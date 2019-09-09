# Flask server
## Build from dockerfile 
```
docker build -t flask:v1 .
```
## Run container

```
docker run -d -p 5000:5000 flask:v1
```

# Redis
```
docker run --name redis -d -p 6379:6379 redis
```