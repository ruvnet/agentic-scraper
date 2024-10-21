from PyPDF2 import PdfReader
from bs4 import BeautifulSoup
from fastapi import UploadFile
import io

async def process_pdf(file: UploadFile):
    content = await file.read()
    pdf_reader = PdfReader(io.BytesIO(content))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

async def process_html(file: UploadFile):
    content = await file.read()
    soup = BeautifulSoup(content, 'html.parser')
    return soup.get_text()
