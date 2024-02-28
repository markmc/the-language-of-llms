import dotenv
import jinja2
import openai
import sys


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

  Use a new HTML paragraph for each concept. Empasize term in question using HTML bold.
"""
SYSTEM_PROMPT = SYSTEM_PROMPT.strip(' \n').replace('\n', '').replace('  ', ' ')

with open('terms.txt', 'r') as f:
    terms = f.readlines()


dotenv.load_dotenv(API_KEY_ENV_FILE)
client = openai.OpenAI()


slides = []
for term in terms:
    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": term},
        ]
    )
    content = completion.choices[0].message.content
    slides.append(content)
    sys.stderr.write(f"Term: {term}\nContent: {content}\n\n")


env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
template = env.get_template('index.html.jinja')

sys.stdout.write(template.render(slides=slides))
