import aiohttp
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse
import time

# Simple in-memory cache for robots.txt
robots_cache = {}
CACHE_EXPIRY = 3600  # 1 hour

async def check_robots_txt(url: str) -> bool:
    parsed_url = urlparse(url)
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
    
    # Check cache first
    if robots_url in robots_cache:
        cache_time, rp = robots_cache[robots_url]
        if time.time() - cache_time < CACHE_EXPIRY:
            return rp.can_fetch("*", url)
    
    async with aiohttp.ClientSession() as session:
        async with session.get(robots_url) as response:
            if response.status == 200:
                robots_content = await response.text()
                rp = RobotFileParser()
                rp.parse(robots_content.splitlines())
                robots_cache[robots_url] = (time.time(), rp)
                return rp.can_fetch("*", url)
    return True  # If no robots.txt or unable to fetch, assume allowed

# Add more utility functions as needed
