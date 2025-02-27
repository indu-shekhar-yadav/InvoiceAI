
# InvoiceAI - Automated Invoice Processing  
**Live Demo**: [InvoiceAI on Render](https://invoiceai-50xd.onrender.com)  

## Overview  
InvoiceAI is a **Streamlit-based web application** that extracts relevant information from invoices using **Google Gemini AI** and **OCR techniques**. The tool enables businesses and individuals to **automate invoice processing, extract key details, and organize financial data efficiently.**  

## Features  
✅ Upload invoice images (JPG, PNG)  
✅ Extract text & key details (Invoice No, Date, Amount, etc.)  
✅ AI-powered invoice data extraction using Google Gemini  
✅ Supports multiple language  
✅ Easy-to-use web interface with Streamlit  
✅ Deployed on Render for seamless access  

## Tech Stack  
- **Frontend**: Streamlit  
- **Backend**: Python (Flask/Streamlit)  
- **AI Model**: Google Gemini API  
- **Data Processing**: PyPDF2, LangChain, ChromaDB  
- **Deployment**: Render  

## Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/indu-shekhar-yadav/InvoiceAI.git
cd InvoiceAI
```

### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables  
Create a `.env` file and add your **Google API Key** securely:  
```
GOOGLE_API_KEY=your-api-key-here
```

### 4️⃣ Run the Application  
```bash
streamlit run app.py
```

## Deployment on Render  
The project is deployed on [Render](https://render.com/), ensuring **high availability and scalability**. You can access it here:  
 **[InvoiceAI Live](https://invoiceai-50xd.onrender.com)**  

## Contributing  
We welcome contributions! Feel free to open issues, submit PRs, or suggest improvements.  
