#!/bin/bash

case $1 in
    build)
        docker-compose build
        ;;
    start)
        docker-compose up
        ;;
    stop)
        docker-compose stop
        ;;
    startdb)
        docker-compose start db
        ;;
    stopdb)
        docker-compose stop db
        ;;
    shell)
        docker exec -i -t live_scores bash
        ;;
esac
