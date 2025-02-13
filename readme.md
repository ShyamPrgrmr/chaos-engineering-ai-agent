# How to initialize docker host ? 
1. Run below command in your docker host (Note - It is fine if you don't have docker installed on host) to fetch initialization script.
> curl https://raw.githubusercontent.com/ShyamPrgrmr/Performance-testing-ai-agent/refs/heads/main/Node%20Agent/initscript.sh > initscript.sh

2. Then run below command. 
> sudo bash initscript.sh 

3. Once you the setup is completed, run below command to get private key and copy the content. 
> sudo cat /root/ai-agent.pem 

4. Now, create a folder and file `./Tools API/helper/host/creds/passkey.pem` and paste the copied content. 

5. Open `./Tools API/config/docker-host.conf` and paste the hostname or ip in hostname field. 

5. Run the "python main.py". 