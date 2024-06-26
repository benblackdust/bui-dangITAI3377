FROM nvcr.io/nvidia/cuda:12.2.2-cudnn8-devel-ubuntu22.04

#Set Timezone to CDT
ENV TZ=America/Chicago

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Update and upgrade the system
RUN apt-get -y update && apt-get -y upgrade

# Install python3 and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Install tensorflow
RUN pip3 install tensorflow

# Required Python Packages
RUN pip3 install pandas numpy paho-mqtt aiocoap asyncua matplotlib

# Install Mosquitto MQTT Broker
RUN apt-get install -y mosquitto

# Install jupyterlab
RUN pip3 install jupyterlab


WORKDIR /workspace

# Start bash
CMD ["/bin/bash"]
