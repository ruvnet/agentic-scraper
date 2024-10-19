# Agentic Scraper

This project consists of two main components:
1. A CLI-based web scraper
2. A FastAPI-based web scraping API

## Installation

1. Ensure you have Python 3.9+ installed.
2. Clone the repository:
   ```
   git clone https://github.com/ruvnet/agentic-scraper.git
   cd agentic-scraper
   ```
3. Install dependencies:
   ```
   ./install.sh
   ```

## Web Scraper CLI

The CLI-based web scraper provides a command-line interface for scraping websites.

### Usage

To use the web scraper CLI:

```bash
./start.sh [OPTIONS] URL
```

Options:
- `--output-format`: Choose between 'text', 'markdown', or 'json' (default: 'text')
- `--check-robots/--no-check-robots`: Enable/disable robots.txt checking (default: disabled)
- `--async-mode/--sync-mode`: Use async or sync mode (default: sync)
- `--concurrency`: Number of concurrent requests in async mode (default: 1)
- `--output-dir`: Directory to save output files (default: current directory)
- `--render-js/--no-render-js`: Enable/disable JavaScript rendering (default: enabled)
- `--verbose`: Show detailed progress

Example:
```bash
./start.sh --output-format json --async-mode --concurrency 5 https://example.com
```

## FastAPI Web Scraping API

The FastAPI-based web scraping API provides HTTP endpoints for web scraping tasks.

### Starting the API Server

To start the FastAPI server:

1. Navigate to the FastAPI directory:
   ```
   cd fastapi
   ```

2. Start the server:
   ```
   uvicorn main:app --reload
   ```

The API will be available at `http://localhost:8000`.

### API Endpoints

- `POST /search`: Execute a search request
- `POST /pdf-to-text`: Upload and process a PDF or HTML file
- `POST /set-proxy`: Set or update the proxy server configuration
- `GET /search-history`: Retrieve the history of search requests

For detailed API documentation, visit `/docs` after starting the server.

## Development

To run tests:

```bash
pytest tests/
```

## Contributing

Contributions to the Agentic Scraper project are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Disclaimer

Always ensure you have permission to scrape a website and comply with its robots.txt directives and terms of service.
