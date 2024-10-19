from pydantic import BaseModel, HttpUrl, validator
from typing import List

class ScraperConfig(BaseModel):
    urls: List[HttpUrl]
    output_format: str
    check_robots: bool = False
    async_mode: bool = False
    concurrency: int = 1
    output_dir: str = '.'

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
