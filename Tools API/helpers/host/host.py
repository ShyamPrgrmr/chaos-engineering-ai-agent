from pathlib import Path

#This class will maintain SSH to docker-agent host. 

class host:
    def __init__(self, hostname, username):
        try:
            directory = Path()
            filepath = Path(str(directory.absolute()) + str(directory.joinpath("/creds/test.txt")))
            file = open(filepath,"r")

            
           
        except Exception as e:
            print (f"Exception {e}")


if __name__=="__main__":
    host("shyam", "username")