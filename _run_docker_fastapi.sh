#! /usr/bin/env sh
# replace docker image with the name of your docker built
docker stop fastapi
docker rm fastapi
docker run -d --name=fastapi \
    -p 8080:80 \
    -v $PWD/app:/app \
    -v $PWD/start.sh:/start.sh \
    -v $PWD/start-reload.sh:/start-reload.sh \
    fastapi bash -c "/start-reload.sh"
docker logs fastapi --follow
