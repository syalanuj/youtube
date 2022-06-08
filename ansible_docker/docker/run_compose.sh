#!/bin/bash -xue
# Starts the lynx Docker ecosystem.
#
# Usage: ./run_compose.sh [optional docker-compose up flags]

cd $(dirname $0)

#export credentials
export GCP_CREDENTIALS="./external-key.json"
export AIRFLOW_IMAGE="lynx-airflow:latest"
export LOGS_FOLDER="../logs"
export DAGS_FOLDER="../dags"

docker-compose up $@
