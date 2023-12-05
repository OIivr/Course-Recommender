import openai
import os
from dotenv import load_dotenv
import json
import time
load_dotenv()

openai.api_type = "azure"
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_base = "https://tu-openai-api-management.azure-api.net/OLTATKULL"
openai.api_version = "2023-07-01-preview"

# Function to get embeddings


def get_embeddings(query):
    try:
        assert isinstance(query, str), "`query` should be a string"
        response = openai.Embedding.create(
            engine="IDS2023_PIKANI_EMBEDDING",
            model="text-embedding-ada-002",
            input=query
        )
        embedding = response.data[0].embedding
        # ------------------LOGS THE TOKENS-------------------- #
        with open("TOTAL_TOKENS_USED.txt", 'r') as f:
            lines = f.readlines()

        for line in lines:
            if line.startswith('embeddings_tokens_used='):
                total_tokens_used = int(line.split('=')[1])
                break
        tokens = response['usage']['total_tokens']
        total_tokens_used += tokens
        for i, line in enumerate(lines):
            if line.startswith('embeddings_tokens_used='):
                lines[i] = f'embeddings_tokens_used={total_tokens_used}\n'
                break
        with open("TOTAL_TOKENS_USED.txt", 'w') as f:
            f.writelines(lines)
        # ------------------------------------------------------ #
        return embedding, tokens
    except Exception as e:
        print("An error occurred:", e)
        return None


token_counter = 0

query_counter = 0

try:
    new_data = []
    with open("data/dataForEmbeddings.json", 'r') as f:
        data = json.load(f)

    for obj in data:
        query_counter += 1
        if query_counter >= 150:
            time.sleep(61)
            query_counter = 0
        if "embeddings" in obj:
            continue
        else:
            input_str = json.dumps(obj)
            response = get_embeddings(input_str)
            new_obj = {
                "data": input_str,
                "embedding_tokens_used": response[1],
                "embeddings": response[0]
            }
            new_data.append(new_obj)
            print(f'{obj["title"]} Done!')
    with open('data/embeddings.json', 'w') as f:
        json.dump(new_data, f, indent=4)
except Exception as e:
    print(f'An error occurred with {obj["title"]}:', e)
