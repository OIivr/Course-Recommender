import json


def remove_actions():
    # Load the data from the all_data_extended_original.json file
    with open('all_data_extended_original.json') as f:
        data = json.load(f)

    # Remove the "_actions" key from each object
    for obj in data:
        if '_actions' in obj:
            del obj['_actions']

    # Write the modified data back to the all_data_extended.json file
    with open('all_data_extended.json', 'w') as f:
        json.dump(data, f, indent=4)


def removeIrrelevantInfo():
    # Load the data from the all_data_extended_original.json file
    with open('all_data_extended_original.json') as f:
        data = json.load(f)

    # Remove the "_actions" key from each object
    for obj in data:
        if '_actions' in obj:
            del obj['_actions']

    # Write the modified data back to the all_data_extended.json file
    with open('all_data_extended.json', 'w') as f:
        json.dump(data, f, indent=4)

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

removeEstonian()
removeUnneeded()