--
Exercises  whit docker

The docker system prune command will remove all stopped containers, all dangling images, and all unused networks:
```
docker system prune

```


To stop all running containers use the docker container stop command followed by a list of all containers IDs.
```
docker container stop $(docker container ls -aq)
```

Once all containers are stopped you can remove them using the docker container stop command followed by the containers ID list.
```
docker container rm $(docker container ls -aq)
```