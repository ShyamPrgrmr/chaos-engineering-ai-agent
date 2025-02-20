import requests, json
from constants.httpresponses import HTTPResponses
from common.logger import logger

class killContainer:
    def __init__(self, endpoint, killPath, removePath):
        self.endpoint = endpoint
        self.path = killPath
        self.removePath = removePath
    
    def kill(self, id):
        logger.info("Killing the container with id : "+id)
        response = requests.post(self.endpoint + str(self.path).format(id=id))
        if(response.status_code >= 200 and response.status_code <= 299 ):
            resp =  {"status":HTTPResponses.SUCCESS, "response":str(response)}
            logger.info("Container has been killed : " + str(resp))
            self.__remove(id=id)
            return resp
        else:    
            resp =  {"status":HTTPResponses.FAILED, "response": json.dumps(response.json())}
            logger.error("Container killing failed : "+str(resp))
            return resp

    def __remove(self, id):
        logger.info("Removing the container with id : "+id)
        response = requests.delete(self.endpoint + str(self.removePath).format(id=id))
        if(response.status_code >= 200 and response.status_code <= 299 ):
            resp =  {"status":HTTPResponses.SUCCESS, "response":str(response)}
            logger.info("Container has been removed : " + str(resp))
            return resp
        else:    
            resp =  {"status":HTTPResponses.FAILED, "response": json.dumps(response.json())}
            logger.error("Container removing failed : "+str(resp))
            return resp    
    