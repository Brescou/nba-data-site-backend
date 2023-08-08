#!/bin/bash

IMAGE_NAME="my-mongodb-dev"
CONTAINER_NAME="my-mongodb-dev"

build() {
    docker build -t $IMAGE_NAME:latest .
}

run() {
    docker run -d -p 27017:27017 --name $CONTAINER_NAME $IMAGE_NAME:latest
}

stop() {
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
}

case "$1" in
    build)
        build
        ;;
    run)
        run
        ;;
    stop)
        stop
        ;;
    *)
        echo "Usage: $0 {build|run|stop}"
esac
