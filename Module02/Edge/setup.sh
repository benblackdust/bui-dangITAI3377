
#!/bin/sh

apt-get update
apt-get install -y python3-pip curl
pip3 install tflite-runtime
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
usermod -aG docker pi
systemctl restart docker