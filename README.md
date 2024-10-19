# Web Scraper Project: Technical Specifications and Development Implementation Guide

## Table of Contents

1. [Introduction](#introduction)
2. [Technical Specifications](#technical-specifications)
   - [Functional Requirements](#functional-requirements)
   - [Non-Functional Requirements](#non-functional-requirements)
3. [Architecture](#architecture)
   - [High-Level Architecture](#high-level-architecture)
   - [Module Responsibilities](#module-responsibilities)
4. [Technologies and Dependencies](#technologies-and-dependencies)
5. [Project Structure](#project-structure)
6. [Development Setup Guide](#development-setup-guide)
   - [Prerequisites](#prerequisites)
   - [Installing Dependencies](#installing-dependencies)
   - [Running the Scraper](#running-the-scraper)
   - [Running Tests](#running-tests)
7. [Extending the Project](#extending-the-project)
   - [Adding New Features](#adding-new-features)
   - [Improving Performance](#improving-performance)
8. [Conclusion](#conclusion)

---

## Introduction

This guide provides a comprehensive overview of the web scraper project implemented using Python, Beautiful Soup, and Playwright. The scraper is designed to fetch, parse, and output content from web pages, supporting features like asynchronous scraping, concurrency, robots.txt compliance, and multiple output formats. This document outlines the technical specifications and offers a step-by-step guide for setting up and extending the project.

---

## Technical Specifications

### Functional Requirements

1. **CLI Interface**: The scraper should provide a command-line interface (CLI) for user interaction, allowing users to specify URLs and options.
2. **URL Input**: Accept one or more URLs to scrape.
3. **Asynchronous Scraping**: Support asynchronous operations with configurable concurrency levels.
4. **Robots.txt Compliance**: Optionally check robots.txt to ensure compliance before scraping.
5. **Content Parsing**: Extract the page title, main content, and all hyperlinks from the web page.
6. **Output Formats**: Support multiple output formats—plain text, Markdown, and JSON.
7. **Error Handling**: Gracefully handle errors during scraping and output operations.
8. **Logging**: Provide informative logging throughout the scraping process.
9. **Configuration**: Allow configuration of scraper behavior through command-line options.

### Non-Functional Requirements

1. **Performance**: Efficiently handle multiple concurrent scraping tasks without significant performance degradation.
2. **Modularity**: Use a modular codebase to facilitate maintenance and future enhancements.
3. **Scalability**: Architected to scale with increased concurrency and additional features.
4. **Usability**: Provide clear and helpful CLI prompts and help messages.
5. **Maintainability**: Write clean, readable code with proper documentation and comments.
6. **Testing**: Include unit tests to ensure code reliability.

---

## Architecture

### High-Level Architecture

The scraper consists of several components, each responsible for a specific part of the scraping process:

- **CLI Interface**: Handles user input and command-line options.
- **Scraper Module**: Manages the fetching of web pages, handling both synchronous and asynchronous operations.
- **Parser Module**: Parses HTML content to extract required data.
- **Output Module**: Formats and saves the scraped data into the specified output format.
- **Utilities Module**: Contains helper functions, such as checking robots.txt.
- **Models Module**: Defines data models using Pydantic for validation and serialization.

### Module Responsibilities

1. **`cli.py`**:
   - Parses command-line arguments.
   - Initializes the scraper configuration.
   - Orchestrates the scraping process based on user inputs.

2. **`scraper.py`**:
   - Contains functions for synchronous and asynchronous scraping.
   - Manages browser instances using Playwright.
   - Handles concurrency and semaphore control.

3. **`parser.py`**:
   - Parses HTML content using Beautiful Soup.
   - Extracts titles, main content, and hyperlinks.

4. **`output.py`**:
   - Formats the scraped data.
   - Saves the output in the specified format and directory.

5. **`utils.py`**:
   - Checks robots.txt for scraping permissions.
   - Contains additional helper functions like caching.

6. **`models.py`**:
   - Defines `ScraperConfig` for configuration.
   - Defines `ScrapedContent` for the scraped data structure.

7. **`tests/`**:
   - Contains unit tests for the scraper and its components.

---

## Technologies and Dependencies

The project leverages the following technologies and libraries:

- **Python 3.9+**: Programming language.
- **Beautiful Soup 4**: For parsing HTML and XML documents.
- **Playwright**: For browser automation and page rendering.
- **Click**: For creating CLI applications.
- **Pydantic**: For data validation and settings management.
- **aiofiles**: For asynchronous file operations.
- **aiohttp**: For asynchronous HTTP requests.
- **AsyncIO**: For writing concurrent code using the async/await syntax.
- **Poetry**: For dependency management and packaging.

---

## Project Structure

The project is organized as follows:

```
web_scraper/
├── pyproject.toml
├── README.md
├── web_scraper/
│   ├── __init__.py
│   ├── cli.py
│   ├── scraper.py
│   ├── parser.py
│   ├── output.py
│   ├── models.py
│   └── utils.py
└── tests/
    ├── __init__.py
    ├── test_scraper.py
    └── test_parser.py
```

- **`pyproject.toml`**: Contains project metadata and dependencies managed by Poetry.
- **`README.md`**: Provides an overview and instructions for the project.
- **`web_scraper/`**: The main package containing all modules.
- **`tests/`**: Directory for unit tests.

---

## Development Setup Guide

### Prerequisites

- **Python 3.9 or higher**: Ensure Python is installed and added to your system's PATH.
- **Poetry**: Install Poetry for dependency management:

  ```bash
  pip install poetry
  ```

- **Playwright Browsers**: Install the required browsers for Playwright:

  ```bash
  playwright install
  ```

### Installing Dependencies

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/web_scraper.git
   cd web_scraper
   ```

2. **Install Dependencies with Poetry**:

   ```bash
   poetry install
   ```

   This command will create a virtual environment and install all the dependencies specified in `pyproject.toml`.

### Running the Scraper

You can run the scraper using Poetry's run command:

```bash
poetry run web-scraper [OPTIONS]
```

#### Command-Line Options

- **`--url`**: One or more URLs to scrape. This option is required and can be specified multiple times.

  ```bash
  --url https://example.com --url https://anotherexample.com
  ```

- **`--output-format`**: The format for the output files. Choices are `text`, `markdown`, or `json`. Default is `text`.

  ```bash
  --output-format markdown
  ```

- **`--check-robots/--no-check-robots`**: Enable or disable checking robots.txt before scraping. Default is `False` (disabled).

  ```bash
  --check-robots
  ```

- **`--async-mode/--sync-mode`**: Run the scraper in asynchronous or synchronous mode. Default is `--sync-mode`.

  ```bash
  --async-mode
  ```

- **`--concurrency`**: Number of concurrent requests when running in async mode. Default is `1`.

  ```bash
  --concurrency 5
  ```

- **`--output-dir`**: Directory to save the output files. Default is the current directory (`.`).

  ```bash
  --output-dir ./scraped_data
  ```

#### Examples

1. **Scrape a Single URL in Synchronous Mode**:

   ```bash
   poetry run web-scraper --url https://example.com --output-format text
   ```

2. **Scrape Multiple URLs in Asynchronous Mode with Concurrency**:

   ```bash
   poetry run web-scraper \
     --url https://example.com \
     --url https://anotherexample.com \
     --output-format markdown \
     --async-mode \
     --concurrency 3 \
     --output-dir ./outputs
   ```

### Running Tests

To run the unit tests, use the following command:

```bash
poetry run pytest tests/
```

---

## Extending the Project

### Adding New Features

1. **Implement Additional Output Formats**:

   - Update `output.py` to handle new formats.
   - Modify `ScraperConfig` to include the new format option.

2. **Enhance Parsing Logic**:

   - Modify `parser.py` to extract additional data, such as images, meta descriptions, etc.
   - Update `ScrapedContent` in `models.py` to include new fields.

3. **Add Custom Headers or Proxies**:

   - Update `scraper.py` to accept headers or proxy configurations.
   - Modify the CLI to include new options.

### Improving Performance

1. **Caching**:

   - Implement caching mechanisms to avoid redundant network requests, especially for robots.txt checks.

2. **Optimizing Concurrency**:

   - Fine-tune the concurrency level based on testing and monitoring.
   - Implement rate limiting or backoff strategies to handle rate-limited sites.

3. **Error Recovery**:

   - Enhance error handling to retry failed requests.
   - Log failed URLs for later analysis.

---

## Conclusion

This web scraper project provides a robust foundation for scraping web content using modern Python libraries and best practices. By following this guide, you can set up the project, understand its architecture, and extend it to meet your specific needs. The modular design and use of asynchronous programming make it both efficient and scalable for various scraping tasks.

---

**Note**: Always ensure that you comply with the terms of service and robots.txt directives of websites you scrape. Unauthorized scraping may violate legal and ethical guidelines.

---

# Appendix: Code Snippets

To provide additional clarity, below are key code snippets from the project.

## `pyproject.toml`

```toml
[tool.poetry]
name = "web-scraper"
version = "0.1.0"
description = "A web scraper using Beautiful Soup and Playwright"
authors = ["Your Name <your.email@example.com>"]
license = "MIT"

[tool.poetry.dependencies]
python = "^3.9"
beautifulsoup4 = "^4.10.0"
playwright = "^1.30.0"
click = "^8.1.3"
pydantic = "^1.10.2"
aiofiles = "^0.8.0"
aiohttp = "^3.8.1"

[tool.poetry.dev-dependencies]
pytest = "^7.2.0"
pytest-asyncio = "^0.20.3"

[tool.poetry.scripts]
web-scraper = "web_scraper.cli:main"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

## `models.py`

```python
from pydantic import BaseModel, HttpUrl, validator
from typing import List

class ScraperConfig(BaseModel):
    urls: List[HttpUrl]
    output_format: str
    check_robots: bool = False
    async_mode: bool = False
    concurrency: int = 1

    @validator('output_format')
    def validate_output_format(cls, v):
        if v not in ['text', 'markdown', 'json']:
            raise ValueError('Invalid output format')
        return v

class ScrapedContent(BaseModel):
    url: HttpUrl
    title: str
    content: str
    links: List[HttpUrl]
```

## `cli.py`

```python
import click
import asyncio
from .models import ScraperConfig
from .scraper import scrape_website, scrape_concurrent
from .output import save_output

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
        concurrency=concurrency
    )

    if async_mode:
        asyncio.run(run_async(config, output_dir))
    else:
        asyncio.run(run_sync(config, output_dir))

async def run_async(config: ScraperConfig, output_dir: str):
    results = await scrape_concurrent(config)
    for i, result in enumerate(results):
        if result:
            filename = f"{output_dir}/output_{i}"
            await save_output(result, config.output_format, filename)

async def run_sync(config: ScraperConfig, output_dir: str):
    for url in config.urls:
        config_single = config.copy()
        config_single.urls = [url]
        result = await scrape_website(config_single)
        if result:
            filename = f"{output_dir}/output_{url.replace('://', '_').replace('/', '_')}"
            await save_output(result, config.output_format, filename)

if __name__ == '__main__':
    main()
```

---

# Frequently Asked Questions (FAQ)

**Q1: Can I use this scraper for any website?**

A1: While technically possible, you should always check the website's terms of service and robots.txt file to ensure that you are allowed to scrape their content. Unauthorized scraping can lead to legal consequences.

**Q2: How can I add support for scraping additional data from pages?**

A2: You can modify the `parse_html` function in `parser.py` to extract more data, such as images, meta tags, or other HTML elements.

**Q3: The scraper is slow when scraping many URLs. How can I improve performance?**

A3: Running the scraper in asynchronous mode with an appropriate concurrency level can significantly improve performance. Adjust the `--concurrency` option based on your system's capabilities and the target website's policies.

**Q4: I encounter errors related to the browser when running the scraper. What should I do?**

A4: Ensure that you have installed the required browsers for Playwright using `playwright install`. If the issue persists, check that your Playwright version is compatible with your Python version.

**Q5: How do I run the scraper without using Poetry?**

A5: While Poetry is recommended for managing dependencies, you can manually install the dependencies listed in `pyproject.toml` using `pip` and run the scraper accordingly.

--- 
