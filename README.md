## Deploy celery beat in the master-slave solution to solve the single point failure problem


```shell
$ docker build -t celery-beat-uwsgi .
$ docker network create --subnet=177.7.0.0/16 net-celery-beat
$ docker-compose up -d
```