""" 
* Functions and methods to synthesize data for the embeddings
* Remove unneeded information from the data and keep only the relevant information
* Restructure the data
* Count the number of tokens in the data

"""

import json


def remove_key(item, word):
    if isinstance(item, dict):
        if word in item:
            del item[word]
        for key, value in item.items():
            remove_key(value, word)
    elif isinstance(item, list):
        for element in item:
            remove_key(element, word)


def removeUnneeded():
    with open('data\Courses_FULL.json') as f:
        data = json.load(f)

    for obj in data:
        remove_key(obj, 'phone')
        remove_key(obj, 'address')
        remove_key(obj, 'city')
        remove_key(obj, 'street')
        remove_key(obj, 'level')
        remove_key(obj, 'academic')
        remove_key(obj, 'supports_continuous_learning')
        remove_key(obj, 'webpage_url')
        remove_key(obj, 'notes')
        remove_key(obj, 'structural_unit')

    with open('data\Courses_FULL.json', 'w') as f:
        json.dump(data, f, indent=4)


def removeEstonian():
    with open('data\Courses_FULL.json') as f:
        data = json.load(f)

    for obj in data:
        remove_key(obj, 'et')

    with open('data\Courses_FULL.json', 'w') as f:
        json.dump(data, f, indent=4)


def remove_irrelevat_info():
    with open('data/Courses_FULL.json') as f:
        data = json.load(f)

    for obj in data:
        remove_key(obj, 'state')
        remove_key(obj, 'registration_info')
        remove_key(obj, 'structural_unit_shares')
        remove_key(obj, 'study_groups')
        remove_key(obj, 'study_group_roles')
        remove_key(obj, 'resources')
        remove_key(obj, 'independent_work')
        remove_key(obj, 'grade_preconditions')
        remove_key(obj, 'grade_evaluation')
        remove_key(obj, 'debt_elimination')
        remove_key(obj, 'year')
        remove_key(obj, 'zip')
        remove_key(obj, 'last_update')

    with open('data/Courses_FULL.json', 'w') as f:
        json.dump(data, f, indent=4)


def remove_empty_descriptions():
    with open('data/Courses_FULL.json') as f:
        data = json.load(f)
        for course in data:
            if "schedule" in course and "entries" in course["schedule"] and all(not entry["description"] for entry in course["schedule"]["entries"]):
                remove_key(course, "schedule")

    with open('data/Courses_FULL.json', 'w') as f:
        json.dump(data, f, indent=4)


def keep_responsible_lecturer():
    with open('data/Courses_FULL.json') as f:
        data = json.load(f)

    for course in data:
        if "lecturers" in course["participants"]:
            course["participants"]["lecturers"] = [
                lecturer for lecturer in course["participants"]["lecturers"] if lecturer["is_responsible"]]

    with open('data/Courses_FULL.json', 'w') as f:
        json.dump(data, f, indent=4)


def change_lecturer_structure():
    with open('data/Courses_FULL.json') as f:
        data = json.load(f)

    for course in data:
        if "lecturers" in course["participants"]:
            responsible_lecturer = next(
                (lecturer for lecturer in course["participants"]["lecturers"] if lecturer["is_responsible"]), None)
            if responsible_lecturer:
                course["lecturer"] = {
                    "person_uuid": responsible_lecturer["person_uuid"],
                    "person_name": responsible_lecturer["person_name"]
                }
            del course["participants"]

    with open('data/Courses_FULL.json', 'w') as f:
        json.dump(data, f, indent=4)


# removeEstonian()
# removeUnneeded()
# remove_actions()
# remove_irrelevat_info()

# remove_empty_descriptions()
# remove_last_update()
# keep_responsible_lecturer()
# change_lecturer_structure()


def add_curricula_to_courses():
    with open('data/Courses_with_its_curricula.json') as f:
        curricula_data = json.load(f)

    with open('data/Courses_FULL.json') as f:
        courses_data = json.load(f)

    curricula_dict = {course["course_code"]: course["curriculum_info"]["curricula"]
                      for course in curricula_data if "curriculum_info" in course and "curricula" in course["curriculum_info"]}

    for course in courses_data:
        if "parent_code" in course:
            course["Curricula"] = curricula_dict.get(course["parent_code"], [])

    with open('data/Courses_FULL2.json', 'w') as f:
        json.dump(courses_data, f, indent=4)


# function to remove the key from all objects in the json file
def remove(key):
    with open('data/dataForEmbeddings.json', 'r') as f:
        data = json.load(f)

    for obj in data:
        remove_key(obj, key)

    with open('data/dataForEmbeddings.json', 'w') as f:
        json.dump(data, f, indent=4)


# function to remove the key but keep the siblings of the key
def remove_key_keep_contents(link):
    with open(link, 'r') as f:
        data = json.load(f)

    for obj in data:
        if "target" in obj:
            obj.update(obj["target"])
            del obj["target"]

    with open(link, 'w') as f:
        json.dump(data, f, indent=4)


# remove_key_keep_contents()


# function to count the number of tokens in the json file
def count_tokens(link):
    with open(link, 'r') as f:
        data = json.load(f)

    total_tokens = 0

    for obj in data:
        json_str = str(obj)
        encoding = tiktoken.get_encoding("cl100k_base")
        token_integers = encoding.encode(json_str)
        num_tokens = len(token_integers)
        total_tokens += num_tokens

    print(f"The total number of tokens is {total_tokens}.")
