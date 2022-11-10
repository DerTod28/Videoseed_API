from googleapiclient.discovery import build
from flask_app.settings.config import app_settings

youtube = build('youtube', 'v3', developerKey=app_settings.youtube_api_kei)
