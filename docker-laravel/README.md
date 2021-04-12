# docker-laravel-handson
Based on https://qiita.com/ucan-lab/items/56c9dc3cf2e6762672f4

### Make sure with phpinfo.php
```
[mac] $ echo "<?php phpinfo();" > backend/public/phpinfo.php
```

### Docker Command
```
# build
$ docker-compose up -d --build

# down
$ docker-compose down
```

### Into to container
```
# app server
$ docker-compose exec app bash

# node server
$ docker-compose exec node ash

# db server
$ docker-compose exec db bash
```

### Output server log
```
# log for laravel
$ docker-compose logs

# specific service
$ docker-compose logs -f app
```


### Connect to database management application
![image](https://user-images.githubusercontent.com/20104403/114467672-3b724680-9c25-11eb-97e3-b868b9c0cf09.png)

