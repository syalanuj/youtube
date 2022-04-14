#!/bin/bash -xue
# Builds the Airflow Docker container

cd $(dirname $0)

docker build -t lynx-airflow:latest .
