from pathlib import Path
import paramiko # type: ignore
from constants.constants import PASSKEYFILEPATH, USERNAME
from common.logger import logger, printLOG


#This class will maintain SSH to docker-agent host. 
class DockerHostAgent:
    def __init__(self, hostname, port):
        try:
            logger.info(f"SSH host and username : {hostname}@{USERNAME}.")
            self.__hostname = hostname
            self.__username = USERNAME
            self.port = port
            directory = Path().absolute()
            pa = str(directory) +"/"+ str(Path(PASSKEYFILEPATH))
            path = Path(pa)
            logger.info(f"Reading key file : {path}")
            self.__private_key = paramiko.RSAKey(filename=str(path))
            self.__ssh_client = paramiko.SSHClient()
            self.__ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        except Exception as e:
            logger.error(f"Exception while setting SSH connection : {e}") 

    

    def executeCommand(self, command):
        try:
            logger.info(f"Setting SSH connection to {self.__hostname}@{self.__username}")
            self.__ssh_client.connect(self.__hostname, username=self.__username, pkey=self.__private_key, port=self.port)
            logger.info(f"SSH connection established successfully.")
            logger.info(f"Running the command through SSH : {command}")
            stdin, stdout, stderr = self.__ssh_client.exec_command(command)
            out = stdout.read().decode()
            err = stderr.read().decode()
            printLOG(out, err)
            self.__ssh_client.close()
            return out, err
        except Exception as e:
            logger.error(f"Exception while executing SSH connection : {e}")

    def executeCommands(self, commands):
        try:
            outputs = []
            logger.info(f"Setting SSH connection to {self.__hostname}@{self.__username}")
            self.__ssh_client.connect(self.__hostname, username=self.__username, pkey=self.__private_key, port=self.port)
            logger.info(f"SSH connection established successfully.")
            for command in commands:
                logger.info(f"Running the command through SSH : {command}")
                stdin, stdout, stderr = self.__ssh_client.exec_command(command)
                out = stdout.read().decode()
                err = stderr.read().decode()
                printLOG(out, err)
                outputs.append( { "command":command, "output":out, "error":err})

              
            isError = self.__checkErrorIfAny(outputs)
            self.__ssh_client.close()
            
            return outputs
        
        except Exception as e:
            logger.error(f"executeCommands Exception : {e}")

    def __checkErrorIfAny(self, outputs):
        for output in outputs:
            if(len(output["error"]) > 0):
                return True
        return False

if __name__=="__main__":
    DockerHostAgent("DEVELOPER - SHYAM PRADHAN")