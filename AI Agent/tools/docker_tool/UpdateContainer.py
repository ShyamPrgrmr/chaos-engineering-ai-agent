import requests, json
from pathlib import Path
from constants.httpresponses import HTTPResponses
from common.logger import logger

class UpdateContainer:
    def __init__(self, endpoint:str, path:str):
        self.__id:str
        self.__request:str
        self.__path = path
        self.__endpoint = endpoint

    def setId(self, id:str):
        self.__id = id
        

    def setRequest(self, request:str):
        self.__request = request
        

    def getEndpoint(self):
        if(len(self.__id)==0):
            logger.error(f"Container id is empty, please use setID to set container ID")
            return None
        else:
            return(f"{(self.__endpoint) + (self.__path).format(id=self.__id)}")

    def update(self, id:str, request:str):
        self.setId(id)
        self.setRequest(request=request)
        logger.info(f"Container constraint update request : {self.__request} ")
        response = requests.post(self.getEndpoint(), json=json.loads(request), headers={"content-type":"application/json"}) 
        
        #Add tools response log
        if(response.status_code == 500):
            logger.error("Container updation failed : "+str(resp))

        if(response.status_code >= 200 and response.status_code <= 299 ):
            temp = json.dumps(response.json())
            data = json.loads(temp)
            resp =  {"status":HTTPResponses.SUCCESS, "response":data}
            logger.info("Container updation success : "+str(resp))
            return resp
        else:    
            resp =  {"status":HTTPResponses.FAILED, "response": json.dumps(response.json())}
            logger.error("Container updation failed : "+str(resp))
            return resp



