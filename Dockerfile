########################
### FRONTEND BUILDER ###
########################

FROM mhart/alpine-node:15.8.0 AS builder

WORKDIR /app

# To cache dependencies even if the code changes, we install deps
# before copying the rest of the code.
COPY frontend/package.json frontend/yarn.lock ./
RUN yarn install

COPY frontend/ ./
RUN yarn build

#######################
### BACKEND COMMAND ###
#######################

FROM python:3.9.1-alpine

WORKDIR /app

RUN mkdir /data /music

ENV DATA_PATH=/data
ENV BUILT_FRONTEND_DIR=/app/frontend
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN echo '[repertoire]\n\
music_directories = ["/music"]\n\
index_crontab = 0 0 * * *' > /data/config.ini

# For Pillow.
RUN apk add jpeg-dev zlib-dev 
RUN apk add --no-cache --virtual build-deps gcc musl-dev libffi-dev openssl-dev

# To cache dependencies even if the code changes, we install deps
# before copying the rest of the code.
COPY backend/requirements.txt ./
RUN pip install -r requirements.txt

COPY backend/ ./
RUN pip install -e .

RUN apk del build-deps

COPY --from=builder /app/build ./frontend

ENTRYPOINT ["repertoire"]
