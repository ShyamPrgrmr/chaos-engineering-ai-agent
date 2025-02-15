import json

class CreateContainerRequest:
    def __init__(self, name, image, hostport, containerport, ip, network, restartPolicy, volumes):
        self.name = name
        self.image = image
        self.hostport = hostport
        self.containerPort = containerport
        self.ip = ip
        self.network = network
        self.restartPolicy= restartPolicy
        self.volumes= volumes

    def getPorts(self, hostport, containerPort):
        return {
            containerPort : [
                {
                    "HostPort" : hostport
                }
            ]
        }

    def getJson(self):
        object = {
                "Name" : self.name, 
                "Image" : self.image, 
                "ExposedPorts": {
                    self.containerPort: {}
                },
                
                "HostConfig": {
                "PortBindings": self.getPorts(self.hostport, self.containerPort),
                "restartPolicy":{
                    "Name" : self.restartPolicy
                },
                
                "Binds": self.volumes,
                "NetworkMode": self.network
                },
                "NetworkingConfig": {
                "EndpointsConfig": {
                self.network: {
                        "IPAMConfig": {
                            "IPv4Address": self.ip
                        }
                    }
                }
            } 
        }
        
        return json.dumps(object)