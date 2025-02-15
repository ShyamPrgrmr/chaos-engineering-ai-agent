import configparser
from CreateContainer import CreateContainer 
from GetContainers import GetContainers 
from KillContainer import killContainer 
from container_ops_type.ContainerOperations import ContainerOperations as ContainerOPS
from constants.httpresponses import HTTPResponses

import logging
logger = logging.getLogger(__name__)


#Temp 
from container_ops_type.CreateContainerRequest import CreateContainerRequest as CreateRequest


class DockerTool:
    def __init__(self, hostname, proto, api_version):
        self.__parser = configparser.RawConfigParser()
        self.__parser.read("./path-config.ini")
        self.endpoint = self.__getApiEndpoint(hostname, proto, api_version)                
        
        
        self.__createContainer = CreateContainer(self.endpoint, self.__getPath(ContainerOPS.MAIN.value, ContainerOPS.CREATE.value), self.__getPath(ContainerOPS.MAIN.value,ContainerOPS.START.value) )
        #self.__getContainers = GetContainers(self.endpoint, self.__getPath(ContainerOPS.MAIN.value, ContainerOPS.GET.value))
        self.__killContainer = killContainer(self.endpoint, self.__getPath(ContainerOPS.MAIN.value, ContainerOPS.KILL.value), self.__getPath(ContainerOPS.MAIN.value, ContainerOPS.REMOVE.value))

    def createContainer(self, request):
        return self.__createContainer.create(request)

    def startContainer(self, id):
        return self.__createContainer.start(id)
    
    def killContainer(self, id):
        return self.__killContainer.kill(id)

    def __getApiEndpoint(self, hostname, proto, api_version):
        endpoint = proto + "://" + hostname + "/" + api_version
        return endpoint
    
    def __getPath(self, type, subtype):
        return self.__parser.get(type, subtype) 

if __name__=="__main__":
    tool = DockerTool("ip172-18-0-4-cuo91mqim2rg00dgl6u0-2376.direct.labs.play-with-docker.com", "http", "v1.43")
    request = CreateRequest("test-container", "httpd", "8081", "80/tcp","192.168.0.10", "agent-network", "always", [])
    response = tool.createContainer(request=request)
    if(response["status"] == HTTPResponses.SUCCESS):
        id = response["id"]
        tool.startContainer(id)        
        response = tool.killContainer(id=id)
