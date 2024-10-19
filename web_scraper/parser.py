from bs4 import BeautifulSoup
from typing import List, Tuple
from urllib.parse import urljoin

def parse_html(html: str, base_url: str) -> Tuple[str, str, List[str]]:
    soup = BeautifulSoup(html, 'html.parser')
    
    title = soup.title.string if soup.title else "No title found"
    
    main_content = ""
    for p in soup.find_all('p'):
        main_content += p.get_text() + "\n"
    
    links = [link.get('href') for link in soup.find_all('a') if link.get('href')]
    
    # Resolve relative URLs
    links = [urljoin(base_url, link) for link in links]
    
    return title, main_content, links
