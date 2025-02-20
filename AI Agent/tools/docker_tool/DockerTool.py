import configparser
from .CreateContainer import CreateContainer 
from .GetContainers import GetContainers 
from .KillContainer import killContainer 
from .container_ops_type.ContainerOperations import ContainerOperations as ContainerOPS
from constants.constants import DOCKER_API_ENDPOINTS_CONFIG
from common.logger import logger



class DockerTool:
    def __init__(self, hostname, proto, api_version):
        logger.info("Intialized Docker Interface")
        self.__parser = configparser.RawConfigParser()
        self.__parser.read(DOCKER_API_ENDPOINTS_CONFIG)
        self.endpoint = self.__getApiEndpoint(hostname, proto, api_version)
        logger.info("Docker API endpoint is : "+self.endpoint)                
        self.__createContainer = CreateContainer(self.endpoint, self.__getPath(ContainerOPS.MAIN.value, ContainerOPS.CREATE.value), self.__getPath(ContainerOPS.MAIN.value,ContainerOPS.START.value) )
        self.__getContainers = GetContainers(self.endpoint, self.__getPath(ContainerOPS.MAIN.value, ContainerOPS.GET.value))
        self.__killContainer = killContainer(self.endpoint, self.__getPath(ContainerOPS.MAIN.value, ContainerOPS.KILL.value), self.__getPath(ContainerOPS.MAIN.value, ContainerOPS.REMOVE.value))
        logger.info("Intialized Docker Interface")


    def createContainer(self, request):
        return self.__createContainer.create(request)

    def startContainer(self, id):
        return self.__createContainer.start(id)
    
    def killContainer(self, id):
        return self.__killContainer.kill(id)

    def getContainer(self, id):
        return self.__getContainers.get(id)

    def __getApiEndpoint(self, hostname, proto, api_version):
        endpoint = proto + "://" + hostname + "/" + api_version
        return endpoint
    
    def __getPath(self, type, subtype):
        return self.__parser.get(type, subtype) 

if __name__=="__main__":

    pass
    