


# Commands


## Build from dockerfile 
```
docker build -t trambo_docker:v1 .
```
## Run container

List elements in s3
Note: Is necessary mount volume where we have credentials of aws, for more information see https://itnext.io/docker-in-docker-521958d34efd
```
docker run -d -v C:\Users\Notebook\.aws:/root/.aws trambo_docker:v2 s3 ls
``` 