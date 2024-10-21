from PyPDF2 import PdfReader
from bs4 import BeautifulSoup
from fastapi import UploadFile

async def process_pdf(file: UploadFile):
    pdf_reader = PdfReader(await file.read())
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

async def process_html(file: UploadFile):
    content = await file.read()
    soup = BeautifulSoup(content, 'html.parser')
    return soup.get_text()
