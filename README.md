# Course-Recommender

## About the project

Welcome to Course-Recommender, a project developed as part of the Introduction to Data Science course. This innovative endeavor harnesses the power of OpenAI's GPT-3.5 Language Model (LLM) to build a sophisticated search engine tailored for courses at the University of Tartu. Our journey through the realm of data science has led us to explore, train, and evaluate the model to enhance the course discovery experience.

## Goals

1. **Explore GPT-3.5 Turbo LLM**: Embark on a journey into the intricacies of OpenAI's GPT-3.5 Language Model. We delve into its advanced natural language processing capabilities to create an enriched course search experience.

2. **Train on University of Tartu Data**: Utilize the vast dataset of University of Tartu courses to fine-tune GPT-4 LLM. This step ensures that the model is finely attuned to the specific nuances and requirements of the academic offerings at the University.

3. **Evaluate Model Performance**: Rigorously assess the trained model's performance and the relevance of its responses. This involves testing its ability to recommend courses accurately based on user queries and contextual information.

## Datasets

- **[Courses.json](data/Courses_FULL.json) (18,3MB):** This dataset contains information on all courses available in University of Tartu, including details on the study program to which each course is listed and the prerequisite courses.
- **[Embeddings.json](data/embeddings.json) (165.5MB):** Dataset with text-embeddings for all courses

## Team

Meet the dedicated individuals who have collaborated on this project as part of the Introduction to Data Science course:

- **Joosep Tamm**
- **Oliver Pikani**
- **Mia-Liisa Kello**

Feel free to explore our journey through data science and course recommendation as we showcase the skills and knowledge acquired during this course. Join us on this exciting adventure of leveraging data for intelligent insights and recommendations at the University of Tartu!

## Getting started

### Installation and setup

You will have to have your own OPEN AI's API key

1. Get your API key at https://platform.openai.com/api-keys
2. Clone the repo:

   ```
   git clone https://github.com/OIivr/Course-Recommender.git
   ```

3. All required libraries are listed in requirements.txt file which can be installed all at once:

   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the `src` folder that will hold your API key.
5. Add the following line in the `.env` file:

   ```
   OPENAI_API_KEY=enter_your_API_key
   ```

   Please note that you might also need to change the `openai.api_type`, `openai.api_key`, `openai.api_base` and `openai.api_version` parameters in the `gpt_queries.py` file based on the API key you provide.

## Usage

To run the application, simply run the `gpt_queries.py` file and _Voila!_

All the token usage is being logged and writen in the `TOTAL_TOKENS_USED.txt` file.

Currently the file contain token counts of the original project, so you'll have to reset the counters if you want to keep track of your token usage.

Enjoy!
