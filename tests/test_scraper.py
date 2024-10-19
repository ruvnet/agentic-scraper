import pytest
from web_scraper.models import ScraperConfig
from web_scraper.scraper import scrape_website, scrape_concurrent

@pytest.mark.asyncio
async def test_scrape_website():
    config = ScraperConfig(urls=['https://example.com'], output_format='text')
    result = await scrape_website(config)
    assert result is not None
    assert result.url == 'https://example.com'
    assert result.title != ''
    assert result.content != ''
    assert len(result.links) > 0

@pytest.mark.asyncio
async def test_scrape_concurrent():
    config = ScraperConfig(urls=['https://example.com', 'https://www.python.org'], output_format='text', async_mode=True, concurrency=2)
    results = await scrape_concurrent(config)
    assert len(results) == 2
    for result in results:
        assert result is not None
        assert result.url in config.urls
        assert result.title != ''
        assert result.content != ''
        assert len(result.links) > 0
