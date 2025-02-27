#!/bin/bash

set -e 

echo "Initializing host"

check_docker() {
    if command -v docker &> /dev/null; then
        echo "Docker is already installed."
    else
        echo "Docker is not installed. Installing now..."
        install_docker
    fi
}

install_docker() {
    echo "Installing Docker..."
    mkdir -p /tmp/docker/
    curl https://get.docker.com/ > /tmp/docker/install_docker.sh
    bash /tmp/docker/install_docker.sh
    systemctl start docker 
    docker --version
    echo "Docker installation completed."
}


check_docker

echo "Creating folder structure..."
mkdir -p /tmp/app/
echo "Folder structure created successfully."

echo "Starting Socat proxy container..."
docker run -d --name socat-proxy --restart always -p 2376:2376 -v /var/run/docker.sock:/var/run/docker.sock alpine/socat TCP-LISTEN:2376,fork UNIX-CONNECT:/var/run/docker.sock
echo "Socat proxy container started successfully."


#echo "Creating docker network"
#docker network create --subnet=192.168.0.0/16 agent-network
#echo "Creating docker stats exporter container"
#docker run -p 9487:9487 --network agent-network --ip 192.168.0.10 -d --name data-exporter --restart always -v /var/run/docker.sock:/var/run/docker.sock wywywywy/docker_stats_exporter
#echo "Creating prometheus server"
#curl https://raw.githubusercontent.com/ShyamPrgrmr/Performance-testing-ai-agent/refs/heads/main/Node%20Agent/prometheus/prmoetheus.yaml > /tmp/prometheus/prometheus.yml
#docker run --name prometheus --network agent-network --restart always -d -p 9090:9090 -v /tmp/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml  prom/prometheus
#echo "Initialization completed."