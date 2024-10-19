import click
import asyncio
import logging
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.text import Text
from web_scraper.models import ScraperConfig
from web_scraper.scraper import scrape_website, scrape_concurrent
from web_scraper.output import save_output

console = Console()

@click.command()
@click.argument('url', nargs=-1, required=True)
@click.option('--output-format', type=click.Choice(['text', 'markdown', 'json']), default='text', help='Output format')
@click.option('--check-robots/--no-check-robots', default=False, help='Check robots.txt before scraping')
@click.option('--async-mode/--sync-mode', default=False, help='Use async mode')
@click.option('--concurrency', default=1, help='Number of concurrent requests (only in async mode)')
@click.option('--output-dir', default='.', help='Directory to save output files')
@click.option('--render-js/--no-render-js', default=True, help='Render JavaScript before scraping')
@click.option('--verbose', is_flag=True, help='Show detailed progress')
def main(url, output_format, check_robots, async_mode, concurrency, output_dir, render_js, verbose):
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

    console.print(Panel(Text("Web Scraper CLI", style="bold magenta"), expand=False))

    with Live(Panel(Text("Initializing...", style="yellow")), refresh_per_second=4) as live:
        if async_mode:
            live.update(Panel(Text("Running in async mode...", style="cyan")))
            asyncio.run(run_async(config, live, verbose))
        else:
            live.update(Panel(Text("Running in sync mode...", style="cyan")))
            asyncio.run(run_sync(config, live, verbose))

    console.print(Panel(Text("Scraping completed", style="bold green"), expand=False))

async def run_async(config: ScraperConfig, live, verbose):
    try:
        live.update(Panel(Text("Preparing to scrape concurrently...", style="yellow")))
        results = await scrape_concurrent(config)
        for i, result in enumerate(results):
            if result:
                live.update(Panel(Text(f"Saving output for URL {i+1}/{len(results)}...", style="green")))
                filename = f"{config.output_dir}/output_{i}"
                await save_output(result, config.output_format, filename)
                if verbose:
                    console.print(f"Saved output for [cyan]{result.url}[/cyan] to [green]{filename}[/green]")
    except Exception as e:
        console.print(f"[bold red]Error in async scraping:[/bold red] {str(e)}")

async def run_sync(config: ScraperConfig, live, verbose):
    for i, url in enumerate(config.urls):
        try:
            live.update(Panel(Text(f"Scraping URL {i+1}/{len(config.urls)}: {url}", style="yellow")))
            result = await scrape_website(url, config)
            if result:
                live.update(Panel(Text(f"Saving output for URL {i+1}/{len(config.urls)}...", style="green")))
                filename = f"{config.output_dir}/output_{url.replace('://', '_').replace('/', '_')}"
                await save_output(result, config.output_format, filename)
                if verbose:
                    console.print(f"Saved output for [cyan]{url}[/cyan] to [green]{filename}[/green]")
        except Exception as e:
            console.print(f"[bold red]Error scraping {url}:[/bold red] {str(e)}")

if __name__ == '__main__':
    main()
