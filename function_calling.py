import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv() ## load all the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-1.5-flash')


chat = model.start_chat()
prompt = "A beautiful sunset over the city"
response = chat.send_message(prompt)
print(response)

# print(response.text)