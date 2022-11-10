import http

import urllib.request

from flask_restful import Resource
from flask import send_file
from pytube.exceptions import VideoUnavailable
from urllib.error import URLError

from flask_app.settings.client import youtube
from pytube import YouTube
from io import BytesIO

from flask_app.settings.logger import logger

link = 'https://www.youtube.com/watch?v='


class Videos(Resource):
    @staticmethod
    def get(video_id: str):
        request = youtube.videos().list(
            part=['contentDetails', 'snippet'],
            id=video_id
        )

        response = request.execute()
        if not response['items']:
            return {'detail': 'Video with requested id not found.'}, http.HTTPStatus.NOT_FOUND

        video_meta = response['items'][0]

        video_detail = {
            'title': video_meta['snippet']['title'],
            'description': video_meta['snippet']['description'],
            'duration': video_meta['contentDetails']['duration']
        }

        return video_detail


class VideosDownload(Resource):
    @staticmethod
    def get(video_id: str):
        video_url = link + video_id
        try:
            yt = YouTube(video_url)
            buffer = BytesIO()
            streams = yt.streams.filter(file_extension='mp4').get_by_itag(22)
            logger.info(f'Downloading video: {video_url}')
            streams.stream_to_buffer(buffer)
            buffer.seek(0)
        except (VideoUnavailable, URLError):
            logger.debug('YouTube error occurred.')
            return {'detail': 'YouTube error occurred.'}, http.HTTPStatus.BAD_REQUEST
        return send_file(
            path_or_file=buffer,
            download_name=yt.title,
            as_attachment=True,
            mimetype=streams.mime_type,
        )


class VideosThumbnail(Resource):
    @staticmethod
    def get(video_id: str):
        video_url = link + video_id

        try:
            yt = YouTube(video_url)
            thumbnail_url = yt.thumbnail_url
            local_filename, headers = urllib.request.urlretrieve(thumbnail_url)

            logger.info(f'Downloading thumbnail: {thumbnail_url}')

        except (VideoUnavailable, URLError):
            logger.debug('YouTube error occurred.')
            return {'detail': 'YouTube error occurred.'}, http.HTTPStatus.BAD_REQUEST
        return send_file(
            path_or_file=local_filename,
            download_name=yt.title,
            as_attachment=True,
            mimetype=headers.get('Content-Type'),
        )
