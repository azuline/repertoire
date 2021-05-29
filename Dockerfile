# This is a Dockerfile for building production images.

# Frontend builder.
# -----------------

FROM mhart/alpine-node:15.8.0 AS builder

WORKDIR /app

# Dockerhub's build environment is slow as fuck and keeps timing out.
RUN yarn config set network-timeout 300000

# To cache dependencies even if the code changes, we install deps
# before copying the rest of the code.
COPY frontend/package.json frontend/yarn.lock ./
RUN yarn install

COPY frontend/ ./
RUN yarn build

# Backend server.
# ---------------

FROM python:3.9.5-slim-buster

WORKDIR /app

# We don't run repertoire as a privileged user; create the group and user and
# the writeable data directories.
RUN addgroup --gid 10001 repertoire && \
    adduser --uid 10000 --gid 10001 --disabled-password --shell /bin/sh repertoire && \
    mkdir /data /music && \
    chown 10000:10001 /data /music

ENV DATA_PATH=/data
ENV BUILT_FRONTEND_DIR=/app/frontend
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

# Update system
RUN apt-get -y upgrade \
    && apt-get -y upgrade

# To cache dependencies even if the code changes, we install deps
# before copying the rest of the code.
COPY backend/requirements.txt ./
RUN pip install --no-cache -r requirements.txt

# Now copy and install  the rest of the backend.
COPY backend/ ./
RUN pip install -e .

COPY --from=builder /app/build ./frontend

# We don't want to run repertoire as a privileged user.
# Note: The application files are owned by root.
USER 10000:10001

ENTRYPOINT ["repertoire"]
CMD ["start", "--host", "0.0.0.0"]
