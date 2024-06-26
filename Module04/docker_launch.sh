#!/bin/bash

# Check if the user is in the Docker group
if [[ $(id -nG) =~ "docker" ]] ; then
    echo "$USER is in the Docker group"
else
    # Add the current user to the Docker group
    echo "Adding $USER to the Docker group"
    sudo usermod -aG docker $USER
    echo "User added to the Docker group. Restarting Docker..."
    sudo systemctl restart docker
fi

# Get the current path
currentPath=$(pwd)

# Prompt if we should rebuild the container
read -p "Do you want to rebuild the container? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "Rebuilding the container"
    docker build "$currentPath" -t module04
fi

# Added -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix to the docker run command to enable GUI
# Run the Docker container with the dynamic path
docker run -it --rm --gpus=all -p 8888:8888 -p 5000:5000 -v "$currentPath/iiot_simulation:/root/iiot_simulation" --network="host" -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix module04
