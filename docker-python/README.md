# docker-laravel-handson
Based on https://qiita.com/jhorikawa_err/items/fb9c03c0982c29c5b6d5


### Docker Command
```
# build
$ docker-compose up -d --build

# down
$ docker-compose down
```

### Into to container
```
# python3 server
$ docker-compose exec python3 bash
```

### Ruine the world
```
$  docker-compose down --rmi all --volumes --remove-orphans 
```