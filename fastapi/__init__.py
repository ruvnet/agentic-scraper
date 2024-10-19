from main import app
from models import SearchRequest, ProxyConfig
from scraper import scrape_website
from pdf_processor import process_pdf, process_html
from proxy_manager import set_proxy, get_proxy
from history_manager import add_to_history, get_search_history

__all__ = [
    'app',
    'SearchRequest',
    'ProxyConfig',
    'scrape_website',
    'process_pdf',
    'process_html',
    'set_proxy',
    'get_proxy',
    'add_to_history',
    'get_search_history'
]
