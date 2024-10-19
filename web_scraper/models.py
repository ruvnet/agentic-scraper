from pydantic import BaseModel, validator
from typing import List

class ScraperConfig(BaseModel):
    urls: List[str]
    output_format: str
    check_robots: bool = False
    async_mode: bool = False
    concurrency: int = 1
    output_dir: str = '.'
    render_js: bool = True

    @validator('output_format')
    def validate_output_format(cls, v):
        if v not in ['text', 'markdown', 'json']:
            raise ValueError('Invalid output format')
        return v

    @validator('urls', each_item=True, pre=True)
    def validate_url(cls, v):
        if not v.startswith(('http://', 'https://')):
            return f'https://{v}'
        return v

class ScrapedContent(BaseModel):
    url: str
    title: str
    content: str
    links: List[str]
