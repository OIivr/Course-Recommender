import tiktoken
from synthesize_data import remove_key
import json

# method to remove the key from all objects in the json file


def remove(key):
    with open('data/dataForEmbeddings.json', 'r') as f:
        data = json.load(f)

    for obj in data:
        remove_key(obj, key)

    with open('data/dataForEmbeddings.json', 'w') as f:
        json.dump(data, f, indent=4)


# remove("is_enlight_course")

# method to remove the key but keep the siblings of the key
def remove_key_keep_contents():
    with open('data/dataForEmbeddings.json', 'r') as f:
        data = json.load(f)

    for obj in data:
        if "target" in obj:
            obj.update(obj["target"])
            del obj["target"]

    with open('data/dataForEmbeddings.json', 'w') as f:
        json.dump(data, f, indent=4)


# remove_key_keep_contents()


# method to count the number of tokens in the json file
def count_tokens():
    with open('data/dataForEmbeddings.json', 'r') as f:
        data = json.load(f)

    total_tokens = 0

    for obj in data:
        json_str = str(obj)
        encoding = tiktoken.get_encoding("cl100k_base")
        token_integers = encoding.encode(json_str)
        num_tokens = len(token_integers)
        total_tokens += num_tokens

    print(f"The total number of tokens is {total_tokens}.")


count_tokens()
