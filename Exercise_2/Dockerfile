FROM alpine:3.7

LABEL maintainer="Joseph Cáceres<josephccaceres@gmail.com>"
 
# Updating package database
RUN apk update

# Install docker
RUN apk add docker
 
ENTRYPOINT ["docker"]