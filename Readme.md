# Cloud Formation
Trambo Cloud- Exercise with docker
### Author: Jhosef Omar Cáceres Aguilar




## Services

| Service     | Descripción 
| :---          |    :----  
| VPC    | Network configuration     
| AG    | Auto scaling group that contains one or more EC2     
| EFS    | File system that contains the web application     
| LB    |   Load balancer that works together whit the launch configuration
| LC    | Configuration of the specifications of the machine to be launched in the Auto-Scalig group          
```
http://localhost:3000/obtenerEstadoLlegadaPiloto
```


# File - main
Template joining the services listed above.

## Parameters


| Parameter | Description | Type 
| :--- | :---- | :----  
| VPCName | VPC Name | String   
| BucketName | Bucket where the templates are | String stored | String 



## Resources

| Resource | Description | Type 
| :--- | :---- | :----  
| VPC | Network Settings | AWS::CloudFormation::Stack AWS::CloudFormation::Stack 
| EFS | File System | AWS::CloudFormation::Stack | AWS::CloudFormation::Stack
| LaunchConfig | Configuration for auto scaling group | AWS::CloudFormation::Stack | AWS::CloudFormation::Stack
| LoadBalancer | Load Balancer | AWS::CloudFormation::Stack
| WebServerGroup | Auto scaling group | AWS::CloudFormation::Stack


## Diagram of the architecture
![Diagram](AWS.png)
 


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