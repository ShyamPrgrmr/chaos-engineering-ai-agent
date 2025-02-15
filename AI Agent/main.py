from tools.host_tool.DockerHostAgent import DockerHostAgent as DockerHostAgent
import configparser



class ToolsAPI:
    def __init__(self, hostname):
        self.__host = DockerHostAgent(hostname)
        self.__config = configparser.RawConfigParser() 
        self.__config.read("./config/application.ini")
        
    def initDockerHost(self):
        commands = []
        commands.append(self.__config.get("docker_host","download_shell_script"))
        commands.append(self.__config.get("docker_host","run_shell_script"))

        outputs, iserror = self.__host.executeCommands(commands)

if __name__=="__main__":
    parser = configparser.RawConfigParser()
    parser.read("./config/docker-host.ini")
    hostname = parser.get("host", "name")
    tools = ToolsAPI(hostname)
    tools.initDockerHost()

