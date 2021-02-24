# This is a Dockerfile for frontend development.
# The frontend source code should be mounted as /app.

FROM mhart/alpine-node:15.8.0 AS builder

WORKDIR /app

ENV BACKEND_HOST=backend

# To cache dependencies even if the code changes, we install deps
# before copying the rest of the code.
COPY package.json yarn.lock ./
RUN yarn install

CMD ["yarn", "start"]
