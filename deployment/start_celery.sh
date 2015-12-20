#!/bin/bash

exec python /code/manage.py celery -A app worker -l info --concurrency 2 -B
