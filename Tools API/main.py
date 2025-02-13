from helpers.host.DockerHostAgent import DockerHostAgent as DockerHostAgent
import configparser

class ToolsAPI:
    def __init__(self, hostname):
        self.__host = DockerHostAgent(hostname)
        self.__config = configparser.RawConfigParser() 
        self.__config.read("./config/application.ini")
        
    def initDockerHost(self):
        #output, error = self.__host.executeCommand("docker ps")
        commands = []
        commands.append(self.__config.get("docker_host","download_shell_script"))
        commands.append(self.__config.get("docker_host","run_shell_script"))

        outputs, iserror = self.__host.executeCommands(commands)

        if iserror:
            print("Operation unsuccessfull, observer these errors "+ outputs)


if __name__=="__main__":
    tools = ToolsAPI("ec2-44-205-243-53.compute-1.amazonaws.com")
    tools.initDockerHost()

