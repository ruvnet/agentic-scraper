import aiohttp
from bs4 import BeautifulSoup
from models import SearchRequest
from proxy_manager import get_proxy

async def scrape_website(request: SearchRequest):
    proxy = get_proxy() if request.use_proxy else None
    
    async with aiohttp.ClientSession() as session:
        async with session.get(request.url, proxy=proxy, timeout=request.timeout) as response:
            html = await response.text()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    if request.css_selector:
        content = soup.select(request.css_selector)
    else:
        content = soup.get_text()
    
    result = {
        "url": request.url,
        "content": str(content),
    }
    
    if request.gather_links:
        result["links"] = [a['href'] for a in soup.find_all('a', href=True)]
    
    if request.gather_images:
        result["images"] = [img['src'] for img in soup.find_all('img', src=True)]
    
    return result
