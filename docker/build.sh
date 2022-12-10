#!/bin/bash

source ./.env

IMAGE_NAME_TAG=$IMAGE_NAME_PYTHON:$IMAGE_NAME_PYTHON_TAG

if [[ "$(docker container ls -a --filter="status=exited" -q 2> /dev/null)" != "" ]]; then
    docker rm $(docker container ls -a --filter="status=exited" -q)
fi

if [[ "$(docker images "dangling=true" -q 2> /dev/null)" != "" ]]; then
    echo "Remove dangling images"
    docker rmi $(docker images -f "dangling=true" -q)
fi

docker build -t $IMAGE_NAME_TAG .