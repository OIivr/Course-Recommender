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
