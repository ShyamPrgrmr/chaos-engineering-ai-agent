from pathlib import Path
import paramiko # type: ignore

#This class will maintain SSH to docker-agent host. 

class DockerHostAgent:
    def __init__(self, hostname):
        try:

            self.__hostname = hostname
            self.__username = "agent-user"
            directory = Path().absolute()
            path = str(directory) + str(Path("/creds/passkey.pem"))
            self.__private_key = paramiko.RSAKey(filename=path)
            self.__ssh_client = paramiko.SSHClient()
            self.__ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
        except Exception as e:
            print (f"Exception {e}")


    def createConnection(self):
        try:
            self.__ssh_client.connect(self.__hostname, username=self.__username, pkey=self.__private_key)
        except Exception as e:
            print(f"Exception {e}")
            print("Please run initscript.sh on docker host")

    def executeCommand(self, command):
        try:
            shell = self.__ssh_client.invoke_shell()
            output = shell.exec_command(command)
            shell.close()
            return output
        except Exception as e:
            print(f"Exception : {e}")



if __name__=="__main__":
    DockerHostAgent("shyam")