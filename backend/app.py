from fastapi import FastAPI, File, Form, UploadFile, HTTPException
import os
import google.generativeai as genai
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Load environment variables
load_dotenv()

# Configure Gemini AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-pro')

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_gemini_response(input_text: str, image_data: dict, prompt: str):
    response = model.generate_content([input_text, image_data, prompt])
    return response.text if response else "No response received."

def process_image(uploaded_file: UploadFile):
    """Convert uploaded file into image data format for Gemini."""
    try:
        bytes_data = uploaded_file.file.read()
        image_parts = {
            "mime_type": uploaded_file.content_type,
            "data": bytes_data
        }
        return image_parts
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")

@app.get("/")
def home():
    return {"message": "Invoice Extraction API is running"}

@app.post("/extract_invoice")
async def extract_invoice(
    input_text: str = Form(...), 
    uploaded_file: UploadFile = File(...)
):
    try:
        image_data = process_image(uploaded_file)
        input_prompt = """
        Role: You are an expert in invoice analysis with deep understanding of various invoice formats across multiple languages.

        Task: You will receive input images of invoices, and your goal is to accurately extract relevant information and answer questions based on the content of the provided invoice.

        Requirements:
        - Analyze the invoice structure, including headers, line items, totals, tax details, and vendor/customer information.
        - Understand multiple languages and varying invoice layouts.
        - Provide precise and context-aware responses to queries related to the invoice.

        Output: Ensure accuracy, completeness, and clarity in responses while maintaining consistency in data extraction.
        """
        response = get_gemini_response(input_text, image_data, input_prompt)
        return JSONResponse(content={"response": response})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
