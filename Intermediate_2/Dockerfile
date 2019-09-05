FROM alpine:3.7

LABEL maintainer="Joseph Cáceres<josephccaceres@gmail.com>"

# Updating package database
RUN apk update

# Install base and dev packages
RUN apk add --no-cache --virtual .build-deps
RUN apk add bash

# Install awscli
RUN apk -v --update add \
        python \
        py-pip \
        groff \
        less \
        mailcap \
        && \
    pip install --upgrade awscli==1.14.5 s3cmd==2.0.1 python-magic && \
    apk -v --purge del py-pip && \
    rm /var/cache/apk/*

# AWS Credentials
RUN aws --profile default configure set aws_access_key_id "AKIAXFHK42N5EBE3IE2A"
RUN aws --profile default configure set aws_secret_access_key "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"

ENTRYPOINT ["aws"]