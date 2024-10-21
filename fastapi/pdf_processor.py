from PyPDF2 import PdfFileReader
from bs4 import BeautifulSoup
from fastapi import UploadFile

async def process_pdf(file: UploadFile):
    pdf_reader = PdfFileReader(await file.read())
    text = ""
    for page in range(pdf_reader.getNumPages()):
        text += pdf_reader.getPage(page).extractText()
    return text

async def process_html(file: UploadFile):
    content = await file.read()
    soup = BeautifulSoup(content, 'html.parser')
    return soup.get_text()
