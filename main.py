import streamlit as st
from PIL import Image
from PIL import ImageOps

import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def rotate_image(rotations: int):
    global image
    return image.rotate(rotations * 90)

def crop_image(left: int, upper: int, right: int, lower: int):
    global image
    return image.crop((left, upper, right, lower))

def mirror_image():
    global image
    return ImageOps.mirror(image)

def zoom_image(factor: float):
    global image
    width, height = image.size
    new_width, new_height = width * factor, height * factor
    return image.resize((int(new_width), int(new_height)), Image.ANTIALIAS)

def invert_image():
    global image
    return ImageOps.invert(image)

def grayscale_image():
    global image
    return ImageOps.grayscale(image)

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
        "rotate_image": rotate_image,
        "crop_image": crop_image,
        "mirror_image": mirror_image,
        "zoom_image": zoom_image,
        "invert_image": invert_image,
        "grayscale_image": grayscale_image,
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