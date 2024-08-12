import streamlit as st
from PIL import Image

import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def say_hello(name : str) -> None:
    return f"Hello, {name}!"

def rotate_image(rotations: int):
    "Hello World"
    global image
    return image.rotate(rotations * 90)

def call_function(function_call, functions):
    function_name = function_call.name
    function_args = function_call.args
    return functions[function_name](**function_args)

def display_result(result):
    if type(result) == str:
        st.write(result)
    # elif type(result) == Image:
    st.image(result, caption="Result", use_column_width=True)

def process_image(image, prompt):
    pretext = """
    Remember, you are Google's Gemini. You are capable of generating function calls.
    You are a photo editing app. You receive an image and a prompt to manipulate the image in some way. You don't have to manipulate the image yourself, we have other librarires to do that job. You just have to call the appropriate function with the image and prompt as arguments
    """
    functions = {
        "say_hello": say_hello,
        "rotate_image": rotate_image,
    }
    model = genai.GenerativeModel(model_name="gemini-1.5-flash", tools=functions.values())
    response = model.generate_content([image, pretext+prompt])
    part = response.candidates[0].content.parts[0]
    print(part)
    if part.function_call:
        result = call_function(part.function_call, functions)
    print(result)
    display_result(result)

# Streamlit UI
st.title("Image Manipulation with Gemini")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
prompt = st.text_input("Enter your manipulation prompt:")

if uploaded_file is not None and prompt:
    image = Image.open(uploaded_file)
    # image_np = np.array(image)
    
    if st.button("Process Image"):
        results = process_image(image, prompt)
        
        # for i, result in enumerate(results):
        #     st.image(result, caption=f"Result {i+1}", use_column_width=True)