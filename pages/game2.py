# image_riddle.py
import streamlit as st
import replicate
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="Image Riddle Arena")

st.title("🎨 Image Riddle Arena")

PROMPT = "Create a visual riddle representing the concept of time without clocks."

# API KEY REQUIRED
# Source: https://replicate.com/docs
image_url = replicate.run(
    "stability-ai/sdxl",
    input={"prompt": PROMPT}
)

response = requests.get(image_url[0])
img = Image.open(BytesIO(response.content))

st.image(img, caption="What concept does this image represent?")

guess = st.text_input("Your guess:")

if st.button("Reveal"):
    st.write("Expected concept: **Time / Impermanence**")
