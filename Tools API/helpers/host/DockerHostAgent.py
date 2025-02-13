from pathlib import Path
import paramiko # type: ignore

#This class will maintain SSH to docker-agent host. 

class DockerHostAgent:
    def __init__(self, hostname):
        try:
            self.__hostname = hostname
            self.__username = "ai-agent"
            directory = Path().absolute()
            path = str(directory) + str(Path("/helpers/host/creds/passkey.pem"))
            self.__private_key = paramiko.RSAKey(filename=path)
            self.__ssh_client = paramiko.SSHClient()
            self.__ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            print("Initialization of host")
            
        except Exception as e:
            print (f"Constructor Exception {e}")

    def executeCommand(self, command):
        try:
            self.__ssh_client.connect(self.__hostname, username=self.__username, pkey=self.__private_key)
            stdin, stdout, stderr = self.__ssh_client.exec_command(command)
            out = stdout.read().decode()
            err = stderr.read().decode()
            self.__ssh_client.close()
            return out, err
        except Exception as e:
            print(f"executeCommand Exception : {e}")

    def executeCommands(self, commands):
        try:
            outputs = []
            self.__ssh_client.connect(self.__hostname, username=self.__username, pkey=self.__private_key)
            
            for command in commands:
                stdin, stdout, stderr = self.__ssh_client.exec_command(command)
                outputs.append( { "command":command, "output":stdout.read().decode(), "error":stderr.read().decode()})
                
            isError = self.__checkErrorIfAny(outputs)
            self.__ssh_client.close()
            
            return outputs, isError
        
        except Exception as e:
            print(f"executeCommand Exception : {e}")

    def __checkErrorIfAny(self, outputs):
        for output in outputs:
            if(len(output["error"]) > 0):
                print("There is an error while running command: " + output["error"])
                return True
        return False

if __name__=="__main__":
    DockerHostAgent("shyam")