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


check_docker_compose() {
    if command -v docker-compose &> /dev/null; then
        echo "Docker Compose is already installed."
    else
        echo "Docker Compose is not installed. Installing now..."
        install_docker_compose
    fi
}

install_docker_compose() {
    sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    echo "Docker Compose installation completed."
}


check_docker
check_docker_compose



echo "Creating folder structure..."
mkdir -p /tmp/prometheus/
mkdir -p /tmp/jmeter/
mkdir -p /tmp/app/
echo "Folder structure created successfully."



echo "Starting Socat proxy container..."
docker run -d --name socat-proxy --restart always -p 2376:2376 -v /var/run/docker.sock:/var/run/docker.sock alpine/socat TCP-LISTEN:2376,fork UNIX-CONNECT:/var/run/docker.sock
echo "Socat proxy container started successfully."


echo "Creating docker network"

docker network create --subnet=192.168.0.0/16 performance-testing-agent-nwk

echo "Creating docker stats exporter container"

docker run -p 9487:9487 --network performance-testing-agent-nwk --ip 192.168.0.10 -d --name data-exporter --restart always -v /var/run/docker.sock:/var/run/docker.sock wywywywy/docker_stats_exporter

echo "Creating prometheus server"



echo "Initialization completed."