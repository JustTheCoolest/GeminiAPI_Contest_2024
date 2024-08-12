import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv() ## load all the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def say_hello(name: str) -> None:
    return f"Hello, {name}!"

functions = {
    "say_hello": say_hello,
}

model = genai.GenerativeModel(model_name="gemini-1.5-flash", tools=functions.values())
# chat = model.start_chat()
response = model.generate_content(
    "Say hi to Harsha"
)
response.candidates[0].content.parts
def call_function(function_call, functions):
    function_name = function_call.name
    function_args = function_call.args
    return functions[function_name](**function_args)


part = response.candidates[0].content.parts[0]
if part.function_call:
    result = call_function(part.function_call, functions)

print(result)

# print(response.text)

# print(response.text)