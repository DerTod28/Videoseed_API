import os

from pydantic import BaseSettings, Field

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Settings(BaseSettings):
    youtube_api_kei: str = Field(env='YOUTUBE_API_KEY')
    host: str = Field(env='HOST')

    class Config:
        env_file = os.path.join(BASE_DIR, 'settings/.env')
        env_file_encoding = 'utf-8'


app_settings = Settings()
