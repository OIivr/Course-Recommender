import requests
import json

""""

url = "http://ois2.ut.ee/api/trainings?start=1&take=100000"
headers = {
    "Content-Type": "application/json",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(response)
else:
    print(f"Error: {response.status_code}, {response.text}")

"""

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


# Fetch extended course info
def fetch_extended_course_info():
    with open('course_codes.txt') as f:
        course_codes = [line.strip() for line in f]

        all_data = []
        for code in course_codes:
            response = requests.get(f'http://ois2.ut.ee/api/courses/{code}')
            data = response.json()
            all_data.append(data)

    with open('all_data_extended.json', 'w') as f:
        json.dump(all_data, f, indent=2)
