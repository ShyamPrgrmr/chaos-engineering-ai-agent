
mkdir -p /tmp/app/
curl https://raw.githubusercontent.com/ShyamPrgrmr/chaos-engineering-ai-agent/refs/heads/main/Node%20Agent/nginx/nginx.conf > /tmp/app/nginx.conf
curl https://raw.githubusercontent.com/ShyamPrgrmr/chaos-engineering-ai-agent/refs/heads/main/Node%20Agent/prometheus/prmoetheus.yaml > /tmp/app/prometheus.yml
curl https://raw.githubusercontent.com/ShyamPrgrmr/chaos-engineering-ai-agent/refs/heads/main/Node%20Agent/docker-compose.yaml > docker-compose.yaml

docker-compose up -d

