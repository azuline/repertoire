# This is a Dockerfile for building production images.

# Frontend builder.

FROM mhart/alpine-node:15.8.0 AS builder

WORKDIR /app

# To cache dependencies even if the code changes, we install deps
# before copying the rest of the code.
COPY frontend/package.json frontend/yarn.lock ./
RUN yarn install

COPY frontend/ ./
RUN yarn build

# Backend server.

FROM python:3.9.1-alpine

WORKDIR /app

RUN mkdir /data /music

ENV DATA_PATH=/data
ENV BUILT_FRONTEND_DIR=/app/frontend
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN echo '[repertoire]\n\
music_directories = ["/music"]\n\
index_crontab = 0 0 * * *' > /data/config.ini

# To cache dependencies even if the code changes, we install deps
# before copying the rest of the code.
COPY backend/requirements.txt ./
# Need these extra deps for Pillow. Run them all in a single layer to reduce
# the container size.
RUN apk add jpeg-dev zlib-dev \
    && apk add --no-cache --virtual build-deps gcc musl-dev \
    && pip install -r requirements.txt \
    && apk del build-deps

# Now copy and install  the rest of the backend.
COPY backend/ ./
RUN apk add --no-cache --virtual build-deps gcc musl-dev libffi-dev openssl-dev \
    && pip install -e . \
    && apk del build-deps

COPY --from=builder /app/build ./frontend

ENTRYPOINT ["repertoire"]
