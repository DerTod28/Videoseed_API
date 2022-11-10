from flask import Blueprint
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint

from flask_app.api.v1 import youtube_api

bp = Blueprint('videoseed-app', __name__, url_prefix='/v1')

api = Api(bp)

api.add_resource(youtube_api.Videos, '/videos/<video_id>')
api.add_resource(youtube_api.VideosDownload, '/videos/<video_id>/download')
api.add_resource(youtube_api.VideosThumbnail, '/videos/<video_id>/thumbnail')

swaggerui_blueprint = get_swaggerui_blueprint(
    base_url='/docs',
    api_url='/static/openapi.yaml',
    config={
        'app_name': 'Test application'
    },
)
