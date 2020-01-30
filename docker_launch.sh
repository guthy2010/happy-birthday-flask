#!/bin/sh

docker build --build-arg SERVE_PORT=$SERVE_PORT --build-arg ENVIRONMENT=$ENVIRONMENT -t happy-birthday-api .
docker run -d -p $SERVE_PORT:$SERVE_PORT happy-birthday-api