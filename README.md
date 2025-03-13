## Deploy celery beat in the master-slave solution to solve the single point failure problem

### Docker deploy
```shell
$ docker build -t celery-beat-uwsgi .
$ docker network create --subnet=177.7.0.0/16 net-celery-beat
$ docker-compose up -d
```

### ERROR: The -s/--socket option is missing and stdin is not a socket.
```shell
sudo apt update
sudo apt install libssl-dev uuid-dev
pip uninstall uwsgi
pip install uwsgi --no-cache-dir
```