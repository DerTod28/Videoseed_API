import http

import requests

host = 'http://app:5000'

url_api = f'{host}/v1/videos/'


def test_video_meta():
    video_id = 'th5_9woFJmk'
    url = f'{url_api}{video_id}'
    response = requests.get(url)
    assert response.status_code == http.HTTPStatus.OK


def test_video_meta_fake_data():
    video_id = '11-111-111-1111'
    url = f'{url_api}{video_id}'
    response = requests.get(url)
    assert response.status_code == http.HTTPStatus.NOT_FOUND


def test_video_download():
    video_id = 'FlZK1zoVvIY'
    url = f'{url_api}{video_id}/download'
    response = requests.get(url)
    assert response.status_code == http.HTTPStatus.OK


def test_video_download_fake_data():
    video_id = '11-111-111-1111'
    url = f'{url_api}{video_id}/download'
    response = requests.get(url)
    assert response.status_code == http.HTTPStatus.BAD_REQUEST


def test_video_thumbnail():
    video_id = 'FlZK1zoVvIY'
    url = f'{url_api}{video_id}/thumbnail'
    response = requests.get(url)
    assert response.status_code == http.HTTPStatus.OK


def test_video_thumbnail_fake_data():
    video_id = '11-111-111-1111'
    url = f'{url_api}{video_id}/thumbnail'
    response = requests.get(url)
    assert response.status_code == http.HTTPStatus.BAD_REQUEST
