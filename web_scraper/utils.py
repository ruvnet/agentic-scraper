import aiohttp
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse

async def check_robots_txt(url: str) -> bool:
    parsed_url = urlparse(url)
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(robots_url) as response:
            if response.status == 200:
                robots_content = await response.text()
                rp = RobotFileParser()
                rp.parse(robots_content.splitlines())
                return rp.can_fetch("*", url)
    return True  # If no robots.txt or unable to fetch, assume allowed

# Add more utility functions as needed
