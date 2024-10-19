from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import asyncio
import redis.asyncio as redis
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter

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
    
    redis_client = redis.from_url("redis://localhost", encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(redis_client)

@app.post("/search")
@app.get("/search", dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def search(request: SearchRequest):
    try:
        result = await scrape_website(request)
        add_to_history(request.dict())
        return JSONResponse(content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/pdf-to-text")
@app.get("/pdf-to-text", dependencies=[Depends(RateLimiter(times=5, seconds=60))])
async def pdf_to_text(file: UploadFile = File(...)):
    if file.filename.endswith('.pdf'):
        text = await process_pdf(file)
    elif file.filename.endswith('.html'):
        text = await process_html(file)
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type")
    return {"text": text}

@app.post("/set-proxy")
@app.get("/set-proxy", dependencies=[Depends(RateLimiter(times=2, seconds=60))])
async def set_proxy_config(config: ProxyConfig):
    set_proxy(config.proxy_address)
    return {"message": "Proxy configuration updated"}

@app.get("/search-history", dependencies=[Depends(RateLimiter(times=20, seconds=60))])
async def search_history():
    history = get_search_history()
    return {"history": history}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
