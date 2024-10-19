# FastAPI Web Scraper

## Introduction

This FastAPI-based web scraper is an advanced, asynchronous web scraping solution that leverages the power of FastAPI, Pydantic, and asynchronous programming. It provides a robust API for web scraping tasks, PDF/HTML processing, proxy configuration, and search history retrieval.

## Features

- Asynchronous web scraping with customizable parameters
- PDF and HTML file processing
- Proxy server configuration
- Search history tracking
- Pydantic models for request and response validation
- FastAPI for high-performance API endpoints

## Installation

1. Ensure you have Python 3.7+ installed.
2. Clone the repository:
   ```
   git clone https://github.com/yourusername/fastapi-web-scraper.git
   cd fastapi-web-scraper
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Endpoints

### POST /search

Executes a search request based on the provided parameters.

**Parameters:**
- `api_key` (optional): String
- `timeout` (optional): Integer (seconds)
- `css_selector` (optional): String (CSS selector to target specific content)
- `wait_for_selector` (optional): String (CSS selector to wait for)
- `gather_links` (optional): Boolean (whether to gather all links)
- `gather_images` (optional): Boolean (whether to gather all images)
- `use_post_method` (optional): Boolean (to send data using POST)
- `json_response` (optional): Boolean (return results in JSON format)
- `forward_cookie` (optional): String (cookie to forward)
- `use_proxy` (optional): String (proxy server address)
- `bypass_cache` (optional): Boolean (disable cache)
- `stream_mode` (optional): Boolean (stream large content)
- `browser_locale` (optional): String (locale settings)

**Response:** JSON containing the content of the fetched page.

### POST /pdf-to-text

Uploads a local PDF or HTML file for text processing.

**Parameters:** File upload (PDF/HTML)

**Response:** Extracted text or structured HTML content.

### POST /set-proxy

Set or update the proxy server configuration.

**Parameters:**
- `proxy_address`: String (the address of the proxy server)

**Response:** Confirmation of proxy configuration.

### GET /search-history

Retrieves the history of search requests.

**Response:** List of previous searches (stored locally or in a database).

## Development

To run tests:

```bash
pytest tests/
```

## Extending the Project

To add new features or modify existing ones, refer to the module structure:

- `main.py`: FastAPI application and route definitions
- `models.py`: Pydantic models for request/response schemas
- `scraper.py`: Core scraping logic
- `pdf_processor.py`: PDF and HTML processing
- `proxy_manager.py`: Proxy configuration management
- `history_manager.py`: Search history tracking

## License

This project is licensed under the MIT License.

## Disclaimer

Always ensure you have permission to scrape a website and comply with its robots.txt directives and terms of service.
