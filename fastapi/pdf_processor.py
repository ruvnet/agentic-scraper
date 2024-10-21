from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError
from bs4 import BeautifulSoup
from fastapi import UploadFile, HTTPException
import io

async def process_pdf(file: UploadFile):
    content = await file.read()
    try:
        pdf_reader = PdfReader(io.BytesIO(content))
        
        if pdf_reader.is_encrypted:
            # If the PDF is encrypted, try to decrypt it with an empty password
            # You may need to modify this part if the PDF requires a specific password
            pdf_reader.decrypt('')

        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except PdfReadError as e:
        raise HTTPException(status_code=400, detail=f"Error reading PDF: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the PDF: {str(e)}")

async def process_html(file: UploadFile):
    content = await file.read()
    soup = BeautifulSoup(content, 'html.parser')
    return soup.get_text()
