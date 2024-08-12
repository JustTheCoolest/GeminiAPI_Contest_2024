import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv() ## load all the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def say_hello(name):
    return f"Hello, {name}!"

model = genai.GenerativeModel('gemini-1.5-flash', tools = [say_hello])

# chat = model.start_chat()
prompt = "Say hi to Harsha"
response = model.generate_content(prompt)
print(response)
# print(response.text)

# print(response.text)