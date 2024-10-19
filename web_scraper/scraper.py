import asyncio
import logging
from typing import List
from playwright.async_api import async_playwright
from .models import ScraperConfig, ScrapedContent
from .utils import check_robots_txt
from .parser import parse_html
from urllib.parse import urlparse

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def scrape_website(config: ScraperConfig) -> ScrapedContent:
    url = config.urls[0]
    logger.info(f"Starting to scrape {url}")
    if config.check_robots and not await check_robots_txt(url):
        logger.warning(f"Scraping not allowed for {url}")
        return None

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        try:
            await page.goto(url)
            html_content = await page.content()
        except Exception as e:
            logger.error(f"Error scraping {url}: {str(e)}")
            return None
        finally:
            await browser.close()

    title, content, links = parse_html(html_content, url)
    
    # Filter out invalid URLs
    valid_links = [link for link in links if urlparse(link).scheme in ['http', 'https']]
    
    logger.info(f"Successfully scraped {url}")
    return ScrapedContent(url=url, title=title, content=content, links=valid_links)

async def scrape_concurrent(config: ScraperConfig) -> List[ScrapedContent]:
    semaphore = asyncio.Semaphore(config.concurrency)
    async def scrape_with_semaphore(url):
        async with semaphore:
            return await scrape_website(ScraperConfig(urls=[url], **config.dict()))
    
    tasks = [scrape_with_semaphore(url) for url in config.urls]
    return await asyncio.gather(*tasks)
