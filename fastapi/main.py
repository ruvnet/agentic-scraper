from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional
import asyncio

from models import SearchRequest, ProxyConfig
from scraper import scrape_website
from pdf_processor import process_pdf, process_html
from proxy_manager import set_proxy, get_proxy
from history_manager import add_to_history, get_search_history
from config import settings

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    if settings.PROXY_ENABLED:
        set_proxy(settings.DEFAULT_PROXY)

@app.post("/search")
@app.get("/search")
async def search(request: SearchRequest):
    try:
        result = await scrape_website(request)
        add_to_history(request.dict())
        return JSONResponse(content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/pdf-to-text")
async def pdf_to_text(file: UploadFile = File(...)):
    if file.filename.endswith('.pdf'):
        text = await process_pdf(file)
    elif file.filename.endswith('.html'):
        text = await process_html(file)
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type")
    return {"text": text}

@app.post("/set-proxy")
@app.get("/set-proxy")
async def set_proxy_config(config: ProxyConfig):
    set_proxy(config.proxy_address)
    return {"message": "Proxy configuration updated"}

@app.get("/search-history")
async def search_history():
    history = get_search_history()
    return {"history": history}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
