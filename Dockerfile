########################
### FRONTEND BUILDER ###
########################

FROM mhart/alpine-node:15 AS builder

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

FROM python:3.8-slim

WORKDIR /app

RUN mkdir /data /music

ENV DATA_PATH=/data
ENV BUILT_FRONTEND_DIR=/app/frontend

RUN echo '[repertoire]\n\
music_directories = ["/music"]\n\
index_crontab = 0 0 * * *' > /data/config.ini

# To cache dependencies even if the code changes, we install deps
# before copying the rest of the code.
COPY backend/requirements.txt ./
RUN pip install -r requirements.txt

COPY backend/ ./
RUN pip install -e .

COPY --from=builder /app/build ./frontend

ENTRYPOINT ["repertoire"]
