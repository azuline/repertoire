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
RUN mkdir /data

ENV DATA_PATH=/data
ENV BUILT_FRONTEND_DIR=/app/frontend

RUN pip install poetry

COPY backend/ .

# TODO: Not sure how to cache dependencies before we copy in the rest of the source?

RUN poetry install --no-root --no-dev

COPY --from=builder /app/build ./frontend

ENTRYPOINT ["poetry", "run", "repertoire"]
