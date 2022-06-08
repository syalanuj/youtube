#!/bin/bash -xue

# Initializes the Airflow database
airflow db init
# Initializes the Airflow database
USER_ID=${HOST_USER_ID:-9001}

# Adds user "user" and executes the Dockerfile's command as "user"
echo "Starting with UID: $USER_ID"
id -u user &>/dev/null || useradd --shell /bin/bash -u $USER_ID -o -c "" -m user

chown -R user:user /home/user

exec gosu user "$@"
