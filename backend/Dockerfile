# This Dockerfile is for backend development.
# The backend source code should be mounted as /app/backend.

FROM python:3.9.1-alpine

WORKDIR /app/backend

RUN mkdir /data /music

ENV DATA_PATH=/data
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
ENV QUART_DEBUG=1
ENV QUART_APP="src.webserver.app:create_app()"

RUN echo '[repertoire]\n\
music_directories = ["/music"]\n\
index_crontab = 0 0 * * *' > /data/config.ini

# Install necessary deps and developer toolings.
RUN apk add jpeg-dev zlib-dev gcc musl-dev libffi-dev openssl-dev make sqlite ack entr

# Install Poetry.
RUN pip install poetry==1.1.4 \
    && poetry config virtualenvs.create false

CMD exec ack -g ".py" \
        --ignore-dir ".mypy_cache" \
        --ignore-dir ".pytest_cache" \
        --ignore-dir "repertoire.egg-info" \
        --ignore-dir "htmlcov" \
    | entr quart run --host 0.0.0.0
