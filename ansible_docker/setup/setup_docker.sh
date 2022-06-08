
   
#! /bin/bash
# This is script is intended to be provided as startup-script for the Google Cloud VM to install docker

#adding docker repo
sudo apt-get -y config-manager \
--add-repo=https://download.docker.com/linux/centos/docker-ce.repo

# install docker 
sudo apt-get -y install  docker-ce docker-ce-cli containerd.io

# start docker service
sudo systemctl start docker

#install docker compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

SERVICE_USER=syal
sudo su
usermod - aG wheel ${SERVICE_USER}
sed -i 's/%sudo\s\+ALL=(ALL:ALL)\s\+ALL/%sudo  ALL=(ALL:ALL) NOPASSWD: ALL/' /etc/sudoers