#!/bin/bash
# This script will run to setup the docker node.   

set -e  # Exit on any error

# Step 1: Install the latest version of Docker
echo "Installing Docker..."

mkdir -p /tmp/docker/
curl https://get.docker.com/ > /tmp/docker/install_docker.sh
bash install_docker.sh

echo "Docker installation completed."

docker --version

echo "Creating folder structure..."
mkdir -p /tmp/prometheus/
mkdir -p /tmp/jmeter/
mkdir -p /tmp/app/

echo "Folder structure created successfully."

# Step 3: Run Socat proxy container
echo "Starting Socat proxy container..."
docker run -d --rm --name socat-proxy --restart always -p 2376:2376 -v /var/run/docker.sock:/var/run/docker.sock alpine/socat TCP-LISTEN:2376,fork UNIX-CONNECT:/var/run/docker.sock
echo "Socat proxy container started successfully."
