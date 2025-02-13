from helpers.host.DockerHostAgent import DockerHostAgent as DockerHostAgent

class ToolsAPI:
    def __init__(self, hostname):
        self.__host = DockerHostAgent(hostname)
        
    def initDockerHost(self):
        output, error = self.__host.executeCommand("docker ps")
        
        print("Output : " + output)
        print("Error : " + error)

if __name__=="__main__":
    tools = ToolsAPI("ec2-44-205-243-53.compute-1.amazonaws.com")
    tools.initDockerHost()

