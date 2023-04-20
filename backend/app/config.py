import logging
import os

from pydantic import BaseSettings

log = logging.getLogger("uvicorn.error")


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    PROJECT_NAME: str = 'test'
    DB_URL: str = None

    class Config:
        env_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
        env_file_encoding = "utf-8"


settings = Settings()
