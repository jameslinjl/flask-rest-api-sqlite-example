# flask-rest-api-sqlite-example

Playing around with flask, sqlite, and docker as a teaching tool for beginner web development.

1) Install docker for your particular machine: https://docs.docker.com/engine/installation/

2) Build the docker image for the app from inside the repo:
```bash
docker build -t <YOUR_DOCKER_HUB_USERNAME>/flask-rest-api-sqlite-example .
```

3) Start running the app using docker:
```bash
docker run -p 8888:5000 <YOUR_DOCKER_HUB_USERNAME>/flask-rest-api-sqlite-example
```

4) Visit the local app running in container at localhost:8888.
