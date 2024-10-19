import click
import asyncio
import logging
from .models import ScraperConfig
from .scraper import scrape_website, scrape_concurrent
from .output import save_output

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@click.command()
@click.option('--url', multiple=True, required=True, help='One or more URLs to scrape')
@click.option('--output-format', type=click.Choice(['text', 'markdown', 'json']), default='text', help='Output format')
@click.option('--check-robots/--no-check-robots', default=False, help='Check robots.txt before scraping')
@click.option('--async-mode/--sync-mode', default=False, help='Use async mode')
@click.option('--concurrency', default=1, help='Number of concurrent requests (only in async mode)')
@click.option('--output-dir', default='.', help='Directory to save output files')
def main(url, output_format, check_robots, async_mode, concurrency, output_dir):
    """Web scraper using Beautiful Soup and Playwright"""
    config = ScraperConfig(
        urls=list(url),
        output_format=output_format,
        check_robots=check_robots,
        async_mode=async_mode,
        concurrency=concurrency,
        output_dir=output_dir
    )

    logging.info(f"Starting scraper with config: {config}")

    if async_mode:
        asyncio.run(run_async(config))
    else:
        asyncio.run(run_sync(config))

async def run_async(config: ScraperConfig):
    try:
        results = await scrape_concurrent(config)
        for i, result in enumerate(results):
            if result:
                filename = f"{config.output_dir}/output_{i}"
                await save_output(result, config.output_format, filename)
                logging.info(f"Saved output for {result.url} to {filename}")
    except Exception as e:
        logging.error(f"Error in async scraping: {str(e)}")

async def run_sync(config: ScraperConfig):
    for url in config.urls:
        try:
            config_single = config.copy(update={'urls': [url]})
            result = await scrape_website(config_single)
            if result:
                filename = f"{config.output_dir}/output_{url.replace('://', '_').replace('/', '_')}"
                await save_output(result, config.output_format, filename)
                logging.info(f"Saved output for {url} to {filename}")
        except Exception as e:
            logging.error(f"Error scraping {url}: {str(e)}")

if __name__ == '__main__':
    main()
