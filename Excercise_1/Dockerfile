FROM alpine:3.7

LABEL maintainer="Joseph Cáceres<josephccaceres@gmail.com>"

# AWS credentials
#ENV aws_access_key_id 0
#ENV aws_secret_access_key 0

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
#RUN aws --profile default configure set aws_access_key_id ${aws_access_key_id} 
#RUN aws --profile default configure set aws_secret_access_key ${aws_secret_access_key} 

ENTRYPOINT ["aws"]