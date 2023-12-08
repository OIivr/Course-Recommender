import json
import time
import openai
import os
from dotenv import load_dotenv
from getEmbeddings import get_embedding
import numpy as np
from openai.embeddings_utils import cosine_similarity
load_dotenv()

openai.api_type = "azure"
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_base = "https://tu-openai-api-management.azure-api.net/OLTATKULL"
openai.api_version = "2023-07-01-preview"

demo_queries = open("data/gpt_system_content.txt", "r").read()


def process_query(query, data):
    assert isinstance(query, str), "`query` should be a string"
    system_content_message = demo_queries + data
    try:
        response = openai.ChatCompletion.create(
            deployment_id="IDS2023_PIKANI_GPT35",
            model="gpt-3.5-turbo",
            temperature=0.0,  # Setting the temperature
            messages=[{"role": "system", "content": system_content_message},
                      {"role": "user", "content": query}]
        )
        status_code = response["choices"][0]["finish_reason"]
        assert status_code == "stop", f"The status code was {status_code}."
        # --------LOGS THE TOKENS--------- #
        with open("TOTAL_TOKENS_USED.txt", 'r') as f:
            lines = f.readlines()

        for line in lines:
            if line.startswith('gpt_tokens_used='):
                total_tokens_used = int(line.split('=')[1])
                break
        tokens = response['usage']['total_tokens']
        total_tokens_used += tokens
        for i, line in enumerate(lines):
            if line.startswith('gpt_tokens_used='):
                lines[i] = f'gpt_tokens_used={total_tokens_used}\n'
                break
        with open("TOTAL_TOKENS_USED.txt", 'w') as f:
            f.writelines(lines)
        # --------------------------------- #
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print("An error occurred:", e)


def get_k_recommendations(query, k=5):
    with open("data/embeddings.json", 'r') as f:
        data = json.load(f)
    assert isinstance(query, str), "`query` should be a string"
    assert isinstance(k, int), "`k` should be an integer"
    assert k > 0, "`k` should be greater than 0"
    query_embedding, tokens_used = get_embedding(query)
    query_embedding = np.array(query_embedding)
    if query_embedding is None:
        print("An error occurred while fetching the query embeddings.")
        return None
    else:
        similarities = []
        for course in data:
            course_embedding = course['embedding']
            course_embedding = np.array(course_embedding)
            similarity = cosine_similarity(query_embedding, course_embedding)
            similarities.append((course["data"], similarity))

        similarities.sort(key=lambda x: x[1], reverse=True)
        recommendations = [course[0] for course in similarities[:k]]
        recommendations_str = '\n- '.join(recommendations)
        return recommendations_str


def cosine_similarity(embedding1, embedding2):
    assert embedding1.shape == embedding2.shape, "Embeddings should have the same shape"
    similarity = np.dot(embedding1, embedding2) / \
        (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))
    return similarity


i = 0
print("------------COURSE RECOMMENDER----------------")
print("")
print("Hello! How may I help you?")
print("")
query = input("Question: ")
while query != "exit":
    i += 1
    print("")
    top_k = get_k_recommendations(query)
    answer = process_query(query, top_k)
    print("")
    print(f"Answer: ")
    print("")
    print(answer)
    print("")
    time.sleep(1)
    print(f"[{i}] -----------------------------------------")
    print("")
    query = input("Question: ")
print("Bye!")
