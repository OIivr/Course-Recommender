import requests
import json


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
