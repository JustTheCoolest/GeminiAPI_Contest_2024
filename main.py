import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def process_image(image, prompt):
    chat = model.start_chat()
    # chat.send_message([image, prompt])
    print(prompt)
    chat.send_message(prompt)
    response = chat.get_response()
    print(response)


def say_hello(name):
    return f"Hello, {name}!"

def parse_gemini_response(response):
    # This function would parse Gemini's response and return a list of operations
    # This is entirely speculative and would depend on Gemini's actual output format
    return [{'type': 'cut', 'params': {'cut_point': 100}},
            {'type': 'rotate', 'params': {'angle': 90}}]


model = genai.GenerativeModel('gemini-1.5-flash', tools=[say_hello])

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