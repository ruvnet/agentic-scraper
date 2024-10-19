from pydantic import BaseModel
from typing import Optional

class SearchRequest(BaseModel):
    url: str
    api_key: Optional[str] = None
    timeout: Optional[int] = 30
    css_selector: Optional[str] = None
    wait_for_selector: Optional[str] = None
    gather_links: Optional[bool] = False
    gather_images: Optional[bool] = False
    use_post_method: Optional[bool] = False
    json_response: Optional[bool] = True
    forward_cookie: Optional[str] = None
    use_proxy: Optional[str] = None
    bypass_cache: Optional[bool] = False
    stream_mode: Optional[bool] = False
    browser_locale: Optional[str] = None

class ProxyConfig(BaseModel):
    proxy_address: str
