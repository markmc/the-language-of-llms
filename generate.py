import dotenv
import jinja2
import openai
import sys
import html
import yaml


API_KEY_ENV_FILE=".api_key.env"
MODELS=["mydefs", "gpt-3.5-turbo", "gpt-4-turbo-preview"]

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

  Use a new HTML <p> tag for each concept. Empasize term in question using HTML <b> tags.
"""
SYSTEM_PROMPT = SYSTEM_PROMPT.strip(' \n').replace('\n', '').replace('  ', ' ')

with open('terms.txt', 'r') as f:
    terms = f.readlines()

with open('mydefs.yaml', 'r') as f:
    mydefs = yaml.safe_load(f).get('terms', {})

dotenv.load_dotenv(API_KEY_ENV_FILE)
client = openai.OpenAI()

sections = []

sections.append([f"<small>{html.escape(SYSTEM_PROMPT)}</small>"])

for term in terms:
    term = term.strip()
    if not term:
        sections.append(["Deep Breath"])
        continue

    slides = []
    for model in MODELS:
        if model == "mydefs":
            slide_content = "<p>"
            for t in [t.strip() for t in term.split(',')]:
                if not t in mydefs:
                    sys.stderr.write(f"{t} not found\n")
                slide_content += f"</p><p>{mydefs.get(t, {}).get('explanation')}"
            slide_content += "</p>"
            slides.append(slide_content)
        else:
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": term},
                ]
            )
            content = completion.choices[0].message.content
            content += f"<small>{model}</small>"

            slides.append(content)
            sys.stderr.write(f"Term: {term}\nContent: {content}\n\n")

    sections.append(slides)

env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
template = env.get_template('index.html.jinja')

sys.stdout.write(template.render(sections=sections))
