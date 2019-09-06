


# Commands
## Build from dockerfile 
```
docker build -t did:v1 .
```
## Run container

```
docker run -d -v /var/run/docker.sock:/var/run/docker.sock did:v1 --version
```
or
```
docker run -d -v /var/run/docker.sock:/var/run/docker.sock did:v1 pull ubuntu
```