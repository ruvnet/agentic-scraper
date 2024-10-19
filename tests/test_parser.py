from web_scraper.parser import parse_html

def test_parse_html():
    html = """
    <html>
        <head><title>Test Page</title></head>
        <body>
            <p>This is a test paragraph.</p>
            <a href="https://example.com">Example Link</a>
        </body>
    </html>
    """
    base_url = "https://test.com"
    title, content, links = parse_html(html, base_url)
    
    assert title == "Test Page"
    assert "This is a test paragraph." in content
    assert "https://example.com" in links
