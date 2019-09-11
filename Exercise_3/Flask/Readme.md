# Flask server
## Build from dockerfile 
```
docker build -t flask:v1 .
```
# Run container

## Flask
Web application in flask 

```
docker run -d -p 5000:5000 flask:v1
```

## Redis

Database 

```
docker run --name redis -d -p 6379:6379 redis
```


# Aplication

The application is a CRUD developed with python by flask 
It is connected to the Redis database through port 6379 via tcp 
