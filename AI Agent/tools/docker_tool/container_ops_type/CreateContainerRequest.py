import json
from typing import List

class CreateContainerRequest:
    def __init__(self):
        self.request = {}

    def getPorts(self, hostport, containerPort):
        return {
            containerPort+"/tcp" : [
                {
                    "HostPort" : hostport
                }
            ]
        }
    
    def setName(self, name:str):
        self.request.update({"Name":name})
        return self
    
    def setImage(self, image:str):
        self.request.update({"Image":image})
        return self
    
    def setExposedPort(self, containerPort:str):
        self.request.update({
            "ExposedPorts": {
                    containerPort: {}
            }
        })
        return self
    
    def setHostConfig(self, hostPort:str, containerPort:str, restartPolicy:str, binds:List[str], network:str):
        self.request.update({
            "HostConfig": {
                    "PortBindings": self.getPorts(hostPort, containerPort),
                    "restartPolicy":{
                        "Name" : restartPolicy
                    },
                    "Binds": binds,
                    "NetworkMode": network
                }
        })
        return self
    
    def build(self):
        return json.dumps(self.request)
    
