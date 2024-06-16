#!/bin/bash

if [[ $(id -nG) =~ "docker" ]] ; then
    echo "$USER in Docker Group"
else
  # Add the current user to the Docker group
  echo "Adding $USER to the Docker group"
  sudo usermod -aG docker $USER
  echo "User added to the Docker group and restarting Docker"
  sudo systemctl restart docker
fi
#prompt if we should rebuild the container
read -p "Do you want to rebuild the container? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "Rebuilding the container"
    docker build . -t module02-edge --no-cache
fi
docker run -it --rm -p 8888:8888 -p 5000:5000 -p 2222:22 -v /home/adam/GitRepos/ITAI-3377/Module02/Edge/notebooks:/root/notebooks module02-edge