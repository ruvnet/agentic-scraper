from bs4 import BeautifulSoup
from typing import List, Tuple
from urllib.parse import urljoin, urlparse

def is_valid_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def parse_html(html: str, base_url: str) -> Tuple[str, str, List[str]]:
    soup = BeautifulSoup(html, 'html.parser')
    
    title = soup.title.string if soup.title else "No title found"
    
    main_content = soup.get_text(separator='\n', strip=True)
    
    links = [link.get('href') for link in soup.find_all('a') if link.get('href')]
    
    # Resolve relative URLs and filter out invalid ones
    links = [urljoin(base_url, link) for link in links]
    links = [link for link in links if is_valid_url(link)]
    
    return title, main_content, links
