# Videoseed_API

Загрузка видео происходит в формате mp4, 720p
Устанавливается локально на компьютер

# Задание
Реализовать REST API в виде микросервиса по работе с API YouTube.

Функционал должен содержать несколько эндпоинтов:

Получение данных о видео по ID (название, описание, длина);
Скачивание видео по ID;
Скачивание превью-картинки видео по ID.

Микросервис должен иметь документацию в Swagger и быть завернут в Docker-контейнер.
Функционал должен быть минимально покрыт UNIT-тестами.
Можно использовать любой фреймворк на Golang или Python (в зависимости от вакансии).

Результаты работы необходимо представить в виде ссылки на репозиторий Github.



## Первый запуск

Воспользуйтесь командой `precommit`, чтобы установить pre-commit хуки

```shell
make precommit
```

Установите poetry

```shell
pip install poetry
```

Установите библиотеки

```shell
poetry install
```


Mac error:

<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed:
unable to get local issuer certificate (_ssl.c:997)>
Go to /Applications/Python3.x and run 'Install Certificates.command'


Curl example
```curl
curl -X 'GET' \
  'http://127.0.0.1:5000/api/v1/videos/vYubIZOyLfI' \
  -H 'accept: application/json'
```

Kill all xxxx ports

```shell
kill -9 $(lsof -i:5000 -t) 2> /dev/null
```
