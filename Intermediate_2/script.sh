#! /bin/bash


# Compiling a docker file
docker build --build-arg aws_access_key_id="AKIAXFHK42N5EBE3IE2A"  --build-arg aws_secret_access_key="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"  -t trambo_docker:v3 .

# Execute a container
docker run -d --rm trambo_docker:v2 s3 ls

#Show logs
docker logs