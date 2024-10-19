import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    API_KEY: str = os.getenv("API_KEY", "default_api_key")
    MAX_CONCURRENT_REQUESTS: int = 10
    DEFAULT_TIMEOUT: int = 30
    MAX_HISTORY_SIZE: int = 100
    PROXY_ENABLED: bool = False
    DEFAULT_PROXY: str = ""
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost")
    RATE_LIMIT_SEARCH: int = 10
    RATE_LIMIT_PDF: int = 5
    RATE_LIMIT_PROXY: int = 2
    RATE_LIMIT_HISTORY: int = 20

    class Config:
        env_file = ".env"

settings = Settings()
