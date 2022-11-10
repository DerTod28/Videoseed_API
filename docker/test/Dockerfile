ARG IMAGE_NAME=python:3.10
FROM ${IMAGE_NAME} as requirements-stage
ARG MODE
WORKDIR /tmp
COPY pyproject.toml poetry.lock /tmp/

ENV POETRY_VERSION=1.2

# System deps:
RUN pip install "poetry==${POETRY_VERSION}"

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes $(test "$MODE" = "DEV" && echo "--with dev")
FROM ${IMAGE_NAME}

ENV WORKDIR_NAME=app
WORKDIR /${WORKDIR_NAME}

COPY --from=requirements-stage /tmp/requirements.txt /${WORKDIR_NAME}/requirements.txt
RUN pip install --no-cache-dir -r /${WORKDIR_NAME}/requirements.txt

COPY . ${WORKDIR}

EXPOSE 5000

CMD ["gunicorn", "--worker-class", "gevent", "--bind", "0.0.0.0:5000", "flask_app.wsgi_app:app"]
CMD ["pytest"]
