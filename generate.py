import dotenv
import openai

API_KEY_ENV_FILE=".api_key.env"
MODEL="gpt-3.5-turbo"

SYSTEM_PROMPT="""
  You are a friendly Computer Science university lecturer who enjoys taking difficult concepts
  and making them as simple as possible.

  You are addressing a 1st year class who are already familiar with many Computer Science concepts.

  Your goal is to introduce the unfamiliar terminology and concepts that the students will encounter
  when studying Machine Learning.

  Your presentation is titled 'The Language of Large Language Models', and you are going to explain
  each individual concept very simply, in less than 20 seconds each.

  You will be provided a term or list of terms, and you will provide that simple explanation in
  return.
"""
SYSTEM_PROMPT = SYSTEM_PROMPT.strip(' \n').replace('\n', '').replace('  ', ' ')

dotenv.load_dotenv(API_KEY_ENV_FILE)

client = openai.OpenAI()

completion = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "'gradient descent', 'stochastic gradient descent (SGD)'"},
    ]
)

print(completion.choices[0].message)
