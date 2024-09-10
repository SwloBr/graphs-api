
import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    db_username: str = os.getenv('DB_USERNAME')
    db_password: str = os.getenv('DB_PASSWORD')
    db_host: str = os.getenv('DB_HOST')
    db_port: str = os.getenv('DB_PORT')
    db_name: str = os.getenv('DB_NAME')

    openroute_key: str = os.getenv('OPENROUTE_KEY')
    opencage_key: str = os.getenv('OPENCAGE_KEY')

    @property
    def sqlalchemy_database_url(self) -> str:
        return f'postgresql+psycopg://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}'

    class Config:
        env_file = ".env"


settings = Settings()
