# Nginx satic server
## Build from dockerfile 
```
docker build -t nginx:v1 .
```
## Run container

```
docker run -d -p 8000:80 nginx:v1
```

