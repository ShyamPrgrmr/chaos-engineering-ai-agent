import configparser

from constants.constants import APPLICATIONCONFIG, DOCKERHOST, DOWNLOADSHELLSCRIPT, RUNSHELLSCRIPT, DOCKER_HOST_CONFIG
from tools.docker_tool.DockerTool import DockerTool as DockerInterfaceHelper
from tools.host_tool.DockerHostAgent import DockerHostAgent as DockerHostHelper


'''
To run the commands on Docker host use self.__host with execute command method (You can also run docker command with all operations). 
To run container specific operations through interface use DockerHelper. 
'''

class ToolsAPI:
    def __init__(self):
        dockerHostConfig = configparser.RawConfigParser()
        dockerHostConfig.read(DOCKER_HOST_CONFIG)   
        self.hostname = dockerHostConfig.get("host", "name")
        self.sshport = dockerHostConfig.get("host", "port") 
        self.apiVersion = dockerHostConfig.get("docker_api", "api_version")
        self.protocol = dockerHostConfig.get("docker_api", "protocol")
            
     
    def initDockerHost(self):
        dockerHostHelper = DockerHostHelper(self.hostname,int(self.sshport))
        commands = []
        self.__config = configparser.RawConfigParser() 
        self.__config.read(APPLICATIONCONFIG)
        commands.append(self.__config.get(DOCKERHOST,DOWNLOADSHELLSCRIPT))
        commands.append(self.__config.get(DOCKERHOST,RUNSHELLSCRIPT))
        outputs = dockerHostHelper.executeCommands(commands)
        return dockerHostHelper

    def initDockerInterface(self):
        dockerInterfaceHelper = DockerInterfaceHelper(hostname=self.hostname, proto=self.protocol, api_version=self.apiVersion)
        return dockerInterfaceHelper

if __name__=="__main__":
    pass
