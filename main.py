import streamlit as st
import numpy as np
from PIL import Image
import io

import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def say_hello(name : str) -> None:
    return f"Hello, {name}!"

def call_function(function_call, functions):
    function_name = function_call.name
    function_args = function_call.args
    return functions[function_name](**function_args)

def process_image(image, prompt):
    functions = {
        "say_hello": say_hello,
    }
    model = genai.GenerativeModel(model_name="gemini-1.5-flash", tools=functions.values())
    response = model.generate_content(prompt)
    part = response.candidates[0].content.parts[0]
    if part.function_call:
        result = call_function(part.function_call, functions)
    print(result)

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