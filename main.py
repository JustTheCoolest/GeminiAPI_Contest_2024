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

def say_hello(name : str) -> None:
    return f"Hello, {name}!"

model = genai.GenerativeModel('gemini-1.5-flash', tools=[say_hello])

def process_image(image, prompt):
    response = model.generate_content(prompt)
    print(response)

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