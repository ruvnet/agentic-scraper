# FastAPI Web Scraper

This is the FastAPI component of the Web Scraper project. It provides a robust API for web scraping tasks, PDF/HTML processing, proxy configuration, and search history retrieval.

## Features

- Asynchronous web scraping with customizable parameters
- PDF and HTML file processing
- Proxy server configuration
- Search history tracking
- Rate limiting to prevent abuse

## Installation

1. Ensure you have Python 3.9+ installed.
2. Install Redis server (used for rate limiting).
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the Redis server.
2. To start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Endpoints

- `POST /search`: Execute a search request
- `POST /pdf-to-text`: Upload and process a PDF or HTML file
- `POST /set-proxy`: Set or update the proxy server configuration
- `GET /search-history`: Retrieve the history of search requests

For detailed API documentation, visit `/docs` after starting the server.

## Configuration

Environment variables can be set in a `.env` file. See `config.py` for available settings.

## Development

To run tests:

```bash
pytest
```

## License

This project is licensed under the MIT License.

## Disclaimer

Always ensure you have permission to scrape a website and comply with its robots.txt directives and terms of service.
