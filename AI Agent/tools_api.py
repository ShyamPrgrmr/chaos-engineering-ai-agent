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
        
        hostname = dockerHostConfig.get("host", "name")
        apiVersion = dockerHostConfig.get("docker_api", "api_version")
        protocol = dockerHostConfig.get("docker_api", "protocol")
                
        self.dockerInterfaceHelper = DockerInterfaceHelper(hostname=hostname, proto=protocol, api_version=apiVersion)
        self.dockerHostHelper = DockerHostHelper(hostname)


     
    '''
    This method will run "https://raw.githubusercontent.com/ShyamPrgrmr/Performance-testing-ai-agent/refs/heads/main/Node%20Agent/script.sh" file on docker host which will run the prometheus, docker-exporter and socat containers on system. 
    '''
    def initDockerHost(self):
        commands = []
        self.__config = configparser.RawConfigParser() 
        self.__config.read(APPLICATIONCONFIG)
        commands.append(self.__config.get(DOCKERHOST,DOWNLOADSHELLSCRIPT))
        commands.append(self.__config.get(DOCKERHOST,RUNSHELLSCRIPT))
        outputs, iserror = self.dockerHostHelper.executeCommands(commands)

    def initDockerInterface(self):
        pass

if __name__=="__main__":
    pass
