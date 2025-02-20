import requests, json
from constants.httpresponses import HTTPResponses
from common.logger import logger


class GetContainers:
    def __init__(self, endpoint, path):
        self.endpoint = endpoint
        self.path = path
    
    def get(self, id):
        response = requests.get(self.endpoint + str(self.path).format(id=id))

        if( response.status_code >= 200 and response.status_code <= 299 ):
            resp =  {"status":HTTPResponses.SUCCESS, "response":str(response)}
            temp = json.dumps(response.json())
            data = json.loads(temp)
            resp =  {"status":HTTPResponses.SUCCESS, "response":data}
            logger.info("Container details : " + str(resp))
            return resp
        
        else:    
            resp =  {"status":HTTPResponses.FAILED, "response": json.dumps(response.json())}
            logger.error("Error in getting container details : "+str(resp))
            return resp