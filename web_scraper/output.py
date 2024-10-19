import json
import aiofiles
import logging
from .models import ScrapedContent

logger = logging.getLogger(__name__)

async def save_output(content: ScrapedContent, output_format: str, filename: str):
    if output_format == 'text':
        await save_text(content, filename)
    elif output_format == 'markdown':
        await save_markdown(content, filename)
    elif output_format == 'json':
        await save_json(content, filename)
    else:
        raise ValueError(f"Unsupported output format: {output_format}")

async def save_text(content: ScrapedContent, filename: str):
    async with aiofiles.open(f"{filename}.txt", mode='w') as f:
        await f.write(f"URL: {content.url}\n")
        await f.write(f"Title: {content.title}\n\n")
        await f.write(f"Content:\n{content.content}\n\n")
        await f.write("Links:\n")
        for link in content.links:
            await f.write(f"- {link}\n")
    logger.info(f"Saved text output to {filename}.txt (Content length: {len(content.content)})")

async def save_markdown(content: ScrapedContent, filename: str):
    async with aiofiles.open(f"{filename}.md", mode='w') as f:
        await f.write(f"# {content.title}\n\n")
        await f.write(f"URL: {content.url}\n\n")
        await f.write(f"## Content\n\n{content.content}\n\n")
        await f.write("## Links\n\n")
        for link in content.links:
            await f.write(f"- [{link}]({link})\n")

async def save_json(content: ScrapedContent, filename: str):
    async with aiofiles.open(f"{filename}.json", mode='w') as f:
        await f.write(json.dumps(content.dict(), indent=2))
