#!/bin/bash -xue
# Builds the Airflow Docker container

cd $(dirname $0)

docker build -t airflow:latest .

# save docker image as a file
docker save airflow | gzip > airflow.tar.gz