# Web Scraper Project

## Introduction

This web scraper project is implemented using Python, Beautiful Soup, and Playwright. It's designed to fetch, parse, and output content from web pages, supporting features like asynchronous scraping, concurrency, robots.txt compliance, and multiple output formats.

## Installation

1. Ensure you have Python 3.9 or higher installed.
2. Install Poetry:
   ```
   pip install poetry
   ```
3. Clone the repository:
   ```
   git clone https://github.com/yourusername/web_scraper.git
   cd web_scraper
   ```
4. Install dependencies:
   ```
   poetry install
   ```
5. Install Playwright browsers:
   ```
   poetry run playwright install
   ```

## Usage

Run the scraper using the provided `start.sh` script:

```bash
./start.sh [OPTIONS] URL
```

### Options

- `--url`: One or more URLs to scrape (required)
- `--output-format`: Output format (text, markdown, json). Default is text.
- `--check-robots/--no-check-robots`: Enable/disable checking robots.txt before scraping. Default is disabled.
- `--async-mode/--sync-mode`: Run in asynchronous or synchronous mode. Default is sync mode.
- `--concurrency`: Number of concurrent requests in async mode. Default is 1.
- `--output-dir`: Directory to save output files. Default is current directory.

### Example

```bash
./start.sh https://example.com --output-format markdown --async-mode --concurrency 3
```

## Troubleshooting

If you encounter a "URL host invalid" error, ensure that the URL you're trying to scrape is properly formatted and includes the protocol (http:// or https://). The `start.sh` script should automatically add `https://` if not provided, but double-check your input.

## Development

To run tests:

```bash
poetry run pytest tests/
```

## Extending the Project

To add new features or modify existing ones, refer to the module structure:

- `cli.py`: Command-line interface
- `scraper.py`: Core scraping logic
- `parser.py`: HTML parsing
- `output.py`: Output formatting and saving
- `models.py`: Data models
- `utils.py`: Utility functions

## License

This project is licensed under the MIT License.

## Disclaimer

Always ensure you have permission to scrape a website and comply with its robots.txt directives and terms of service.
