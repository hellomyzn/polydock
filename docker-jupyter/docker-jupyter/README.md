### Installation
```
$ docker compose up -d --build
```

### Usage
```
Access: http://localhost:8888 
```


### Docker Command
```
# build
$ docker-compose up -d --build

# down
$ docker-compose down

# ruine the world
$ docker-compose down --rmi all --volumes --remove-orphans 

# if you want to remove <none> images
$ docker image prune
```