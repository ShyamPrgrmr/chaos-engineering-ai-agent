# How to initialize docker host ? 

1. Run `curl https://raw.githubusercontent.com/ShyamPrgrmr/chaos-engineering-ai-agent/refs/heads/main/Node%20Agent/startup.sh > startup.sh` command on your docker host (note - Please make sure that your docker host has docker and docker-compose installed on it).  

2. Run `sh startup.sh` to install required settings. 

3. Now run, `docker-compose up -d` to start containers. 

3. Update your hostname in `./AI Agent/config/docker-host.ini` under host (Append the host with port 80 ex.hostname:80 and do not add any protocol like "http" or "https" in hostname). 
