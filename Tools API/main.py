from helpers.host.DockerHostAgent import DockerHostAgent as DockerHostAgent

class ToolsAPI:
    def __init__(self):
        pass
    
    def initDockerHost(self):
        host = DockerHostAgent("ec2-44-205-243-53.compute-1.amazonaws.com")
        host.createConnection()
        output = host.executeCommand("ls -ltr")
        print(output)

if __name__=="__main__":
    pass

