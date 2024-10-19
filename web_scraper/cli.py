import click
import asyncio
import logging
from tqdm import tqdm
from web_scraper.models import ScraperConfig
from web_scraper.scraper import scrape_website, scrape_concurrent
from web_scraper.output import save_output

# Change the default logging level to WARNING
logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@click.command()
@click.argument('url', nargs=-1, required=True)
@click.option('--output-format', type=click.Choice(['text', 'markdown', 'json']), default='text', help='Output format')
@click.option('--check-robots/--no-check-robots', default=False, help='Check robots.txt before scraping')
@click.option('--async-mode/--sync-mode', default=False, help='Use async mode')
@click.option('--concurrency', default=1, help='Number of concurrent requests (only in async mode)')
@click.option('--output-dir', default='.', help='Directory to save output files')
@click.option('--render-js/--no-render-js', default=True, help='Render JavaScript before scraping')
@click.option('--quiet', is_flag=True, help='Suppress most output')
@click.option('--show-progress', is_flag=True, help='Show progress bar')
def main(url, output_format, check_robots, async_mode, concurrency, output_dir, render_js, quiet, show_progress):
    """Web scraper using Beautiful Soup and Playwright"""
    config = ScraperConfig(
        urls=list(url),
        output_format=output_format,
        check_robots=check_robots,
        async_mode=async_mode,
        concurrency=concurrency,
        output_dir=output_dir,
        render_js=render_js
    )

    if quiet:
        logging.getLogger().setLevel(logging.ERROR)
    
    if not quiet:
        print(f"Starting scraper for {len(config.urls)} URL(s)")

    if async_mode:
        asyncio.run(run_async(config, show_progress))
    else:
        asyncio.run(run_sync(config, show_progress))

    if not quiet:
        print("Scraping completed")

async def run_async(config: ScraperConfig, show_progress: bool):
    try:
        results = await scrape_concurrent(config)
        for i, result in enumerate(results):
            if result:
                filename = f"{config.output_dir}/output_{i}"
                await save_output(result, config.output_format, filename)
                if not show_progress:
                    logger.info(f"Saved output for {result.url} to {filename}")
    except Exception as e:
        logger.error(f"Error in async scraping: {str(e)}")

async def run_sync(config: ScraperConfig, show_progress: bool):
    for url in (tqdm(config.urls, desc="Scraping progress") if show_progress else config.urls):
        try:
            result = await scrape_website(url, config)
            if result:
                filename = f"{config.output_dir}/output_{url.replace('://', '_').replace('/', '_')}"
                await save_output(result, config.output_format, filename)
                if not show_progress:
                    logger.info(f"Saved output for {url} to {filename}")
        except Exception as e:
            logger.error(f"Error scraping {url}: {str(e)}")

if __name__ == '__main__':
    main()
