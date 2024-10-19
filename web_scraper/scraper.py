import asyncio
from playwright.async_api import async_playwright
from .models import ScraperConfig, ScrapedContent
from .utils import check_robots_txt
from .parser import parse_html

async def scrape_website(config: ScraperConfig) -> ScrapedContent:
    url = config.urls[0]
    if config.check_robots and not await check_robots_txt(url):
        print(f"Scraping not allowed for {url}")
        return None

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        html_content = await page.content()
        await browser.close()

    title, content, links = parse_html(html_content, url)
    return ScrapedContent(url=url, title=title, content=content, links=links)

async def scrape_concurrent(config: ScraperConfig) -> List[ScrapedContent]:
    semaphore = asyncio.Semaphore(config.concurrency)
    async def scrape_with_semaphore(url):
        async with semaphore:
            return await scrape_website(ScraperConfig(urls=[url], **config.dict()))
    
    tasks = [scrape_with_semaphore(url) for url in config.urls]
    return await asyncio.gather(*tasks)
