import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

webcontent = [
  {"topic": "Python 3", "target": "Beginners", "link": "youtube.com/beginners"},
  {"topic": "Python 3 OOP", "target": "Advanced", "link": "youtube.com/oop"},
  {"topic": "FastAPI", "target": "Intermediate", "link": "youtube.com/fastapi"}
]

content = f"""
You are a helpful assistant for my website, where you can learn about coding. Don´t suggest other ressources 
like Codecademy etc. Just my own content. Provide the user the link with the best suited video. Here are my videos:
{str(webcontent)}.
Only answer questions regarding coding. Say 'Please ask google' for anything else.
"""

print("Hello! I'm a helpful assistant for providing information about videos on my channel. How can I assist you today?")
context = [{"role": "system", "content": content}]

while True:
  user_input = input("You: ")
  if user_input.lower() in ["bye", "goodbye", "exit"]:
    print("Assistant: Goodbye!")
    break
  else:
    messages = context + [
      {"role": "user", "content": user_input }
    ]
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages,
    )

    message = response.choices[0].message
    context.append({"role": message["role"], "content": message["content"]})
    print("Assistant:", message["content"])