# This is a Dockerfile for building production images.

# Frontend builder
# ----------------

FROM mhart/alpine-node:15.8.0 AS frontend-builder

WORKDIR /app

# Dockerhub's build environment is slow as fuck and keeps timing out.
RUN yarn config set network-timeout 300000

# To cache dependencies even if the code changes, we install deps
# before copying the rest of the code.
COPY frontend/package.json frontend/yarn.lock ./
RUN yarn install

COPY frontend/ ./
RUN yarn build

# SQLite3 builder
# ---------------

FROM python:3.9.5-buster AS sqlite-builder

WORKDIR /

# RUN apt-get upgrade -y && apt-get install -y curl unzip
# This is to upgrade SQLite3 in our debian container (to 3.35.0).
# Commands from https://charlesleifer.com/blog/compiling-sqlite-for-use-with-python-applications/.

RUN curl -O https://sqlite.org/2021/sqlite-autoconf-3350500.tar.gz \
    && tar -xzf sqlite-autoconf-3350500.tar.gz \
    && mv sqlite-autoconf-3350500 sqlite \
    && cd sqlite \
    && export CFLAGS="-DSQLITE_ENABLE_FTS5 \
        -DSQLITE_ENABLE_JSON1 \
        -DSQLITE_ENABLE_LOAD_EXTENSION \
        -DSQLITE_ENABLE_STAT4 \
        -DSQLITE_ENABLE_UPDATE_DELETE_LIMIT \
        -DSQLITE_TEMP_STORE=3 \
        -DSQLITE_USE_URI \
        -O2 \
        -fPIC" \
    && export PREFIX="/usr/local" \
    && LIBS="-lm" ./configure --enable-shared --prefix="$PREFIX" \
    && make

# Backend server
# --------------

FROM python:3.9.5-buster

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
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install make

# Install upgraded sqlite3
ENV LD_LIBRARY_PATH=/usr/local/lib
COPY --from=sqlite-builder /sqlite /sqlite
RUN cd /sqlite && PREFIX="/usr/local" make install

# To cache dependencies even if the code changes, we install deps
# before copying the rest of the code.
COPY backend/requirements.txt ./
RUN pip install --no-cache -r requirements.txt

# Now copy and install  the rest of the backend.
COPY backend/ ./
RUN pip install -e .

# Copy the built frontend
COPY --from=frontend-builder /app/build ./frontend

# We don't want to run repertoire as a privileged user.
# Note: The application files are owned by root.
USER 10000:10001

ENTRYPOINT ["repertoire"]
CMD ["start", "--host", "0.0.0.0"]
