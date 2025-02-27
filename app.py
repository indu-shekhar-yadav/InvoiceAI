from dotenv import load_dotenv
load_dotenv() 
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Configure Gemini AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-pro')

def get_gemini_response(input_text, image_data, prompt):
    response = model.generate_content([input_text, image_data, prompt])  
    return response.text if response else "No response received."

# Streamlit setup
st.set_page_config(page_title="InvoiceAI")
st.header("Multi-language AI-powered invoice extraction")

def input_image_setup(uploaded_file):
    """Convert uploaded file into image data format for Gemini."""
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = {
            "mime_type": uploaded_file.type,  # Get the mime type (e.g., image/png)
            "data": bytes_data
        }
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# User input
input_text = st.text_input("Input Prompt:", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image_data = None  

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    image_data = input_image_setup(uploaded_file)  # Process image

submit = st.button("Extract Invoice Data")

input_prompt = """
Role: You are an expert in invoice analysis with deep understanding of various invoice formats across multiple languages.

Task: You will receive input images of invoices, and your goal is to accurately extract relevant information and answer questions based on the content of the provided invoice.

Requirements:
- Analyze the invoice structure, including headers, line items, totals, tax details, and vendor/customer information.
- Understand multiple languages and varying invoice layouts.
- Provide precise and context-aware responses to queries related to the invoice.

Output: Ensure accuracy, completeness, and clarity in responses while maintaining consistency in data extraction.
"""

if submit and image_data:
    response = get_gemini_response(input_text, image_data, input_prompt)
    st.subheader("The Response is")
    st.write(response)
