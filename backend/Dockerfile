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
RUN apk add jpeg-dev zlib-dev gcc musl-dev libffi-dev openssl-dev make sqlite

# Install Poetry.
RUN pip install poetry==1.1.4 \
    && poetry config virtualenvs.create false

# To cache dependencies even if the code changes, we install deps
# before copying the rest of the code.
COPY ./pyproject.toml ./poetry.lock ./
RUN mkdir src && touch src/__init__.py
RUN poetry install

CMD ["quart", "run", "--host", "0.0.0.0"]
