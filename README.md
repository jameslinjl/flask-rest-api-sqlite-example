# pokedex-pokeapi-memcache

Playing around with flask, pokeapi, memcached, and docker as a teaching tool for beginner web development.

1) Install docker for your particular machine: https://docs.docker.com/engine/installation/

2) Build the docker image for the app from inside the repo:
```bash
docker build -t <YOUR_DOCKER_HUB_USERNAME>/pokedex-pokeapi-memcache .
```

3) Make sure to configure memcached for docker:
```bash
docker pull memcached # pull the remote memcached docker image
docker run --name my-memcache -d memcached # start running memcached in a container
```

4) Start running the app using docker:
```bash
docker run -p 8888:5000 --link my-memcache:memcache <YOUR_DOCKER_HUB_USERNAME>/pokedex-pokeapi-memcache
```

5) Visit the local app running in container at localhost:8888.
