import requests
import json

# Initial API test


def get_all_courses():
    all_courses = []
    base_url = "http://ois2.ut.ee/api/courses"
    take = 300

    for start in range(1, 4000, take):
        response = requests.get(f"{base_url}?start={start}&take={take}")
        if response.status_code == 200:
            data = response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")

        all_courses.append(data)

    return all_courses


all_courses = get_all_courses()
with open('courses.json', 'w') as output_file:
    json.dump(all_courses, output_file, indent=2)


# Get how many courses there are in the file
with open('courses.json') as f:
    data = json.load(f)

num_courses = len(data)
print(f'There are {num_courses} courses in the file.')


# Extract course codes from the courses.json file
def extract_course_codes():
    # Load JSON data from file
    with open('courses.json', 'r') as json_file:
        data = json.load(json_file)

    # Extract course codes
    course_codes = [item["code"] for item in data if "code" in item]
    # Write course codes to a new text file
    with open('course_codes.txt', 'w') as code_file:
        for code in course_codes:
            code_file.write(f"{code}\n")

    print("Course codes extracted and written to 'course_codes.txt'")


# Fetch the full info for each course
def fetch_extended_course_info():
    with open('data/course_codes.txt') as f:
        course_codes = [line.strip() for line in f]

        error_data = {}
        all_data = []
        for code in course_codes:
            response = requests.get(
                f'http://ois2.ut.ee/api/courses/{code}/versions')
            data = response.json()
            if len(data) > 0:
                newest_version = data[-1]["uuid"]
                response = requests.get(
                    f'http://ois2.ut.ee/api/courses/{code}/versions/{newest_version}')
                data = response.json()
                all_data.append(data)
            else:
                print(f"Error: {response.status_code}, {response.text}")
                error_data[code] = response.text

    with open('Courses(FULL1).json', 'w') as f:
        json.dump(all_data, f, indent=2)
    return error_data


# Fetch curriculum info
def fetch_curriculum_info():
    with open('data/courses (initial).json') as f:
        courses = json.load(f)
        curriculums = []
        for obj in courses:
            uuid = obj["uuid"]
            code = obj["code"]
            response = requests.get(
                f'https://ois2.ut.ee/api/curricula/course/{uuid}')
            curriculum_data = response.json()

            # Create a new dictionary for each course with its curriculum information
            course_with_curriculum = {
                "course_code": code,
                "curriculum_info": curriculum_data
            }
            if len(curriculum_data) > 0:
                curriculums.append(course_with_curriculum)
        return curriculums


curriculums = fetch_curriculum_info()

with open('Curriculums.json', 'w') as f:
    json.dump(curriculums, f, indent=2)
