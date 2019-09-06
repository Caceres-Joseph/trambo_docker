#! /bin/bash


# Compiling a docker file
#docker build --build-arg aws_access_key_id="***"  --build-arg aws_secret_access_key="**"  -t trambo_docker:v4 .
docker build -t trambo_docker:v3 .


# Execute a container
docker run -d --rm -v C:\Users\Notebook\.aws:~/.aws trambo_docker:v2 s3 ls
docker run -d -v C:\Users\Notebook\.aws:/root/.aws trambo_docker:v2 s3 ls

#Show logs
docker logs