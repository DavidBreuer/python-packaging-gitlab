FROM python:3.7-stretch
LABEL maintainer="info <info@info.com>"

ARG SUB_USER
ARG SUB_TOKEN

ARG BUILD_DEPS=" \
    g++"
ARG RUNTIME_DEPS=" \
    make \
    python3-dev"

WORKDIR /app
RUN apt-get update
RUN apt-get install -y --no-install-recommends $BUILD_DEPS $RUNTIME_DEPS
ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ADD ./requirements_dev.txt /app/requirements_dev.txt
RUN pip install -r requirements_dev.txt
RUN apt-get purge --yes $BUILD_DEPS \
    && apt-get autoremove --yes \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/*

ADD . /app
RUN pip install --no-deps .
