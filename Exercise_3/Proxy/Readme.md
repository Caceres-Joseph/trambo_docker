


# Commands
## Build from dockerfile 
```
docker build -t proxy:v1 .
```
## Run container

```
docker run --rm -d -p 8080:80 proxy:v1 
```
or
```
docker run -d -v /var/run/docker.sock:/var/run/docker.sock did:v1 pull ubuntu
```