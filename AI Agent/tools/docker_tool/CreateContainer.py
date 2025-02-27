import requests, json
from constants.httpresponses import HTTPResponses
from common.logger import logger
from constants.constants import APPLICATIONNAME


class CreateContainer():
    def __init__(self, endpoint, createPath, startPath):
        self.path = createPath
        self.startPath = startPath
        self.endpoint = endpoint
        
    def create(self, request):
        logger.info("Creating container with request : "+ str(request))       
        response = requests.post(self.endpoint+self.path+"?name="+APPLICATIONNAME, json=json.loads(request), headers={"content-type":"application/json"}) 
        if(response.status_code >= 200 and response.status_code <= 299 ):
            temp = json.dumps(response.json())
            data = json.loads(temp)
            resp =  {"status":HTTPResponses.SUCCESS, "response":data, "id": data["Id"]}
            logger.info("Container creation successed : " + str(resp))
            return resp
        else:    
            resp =  {"status":HTTPResponses.FAILED, "response": json.dumps(response.json())}
            logger.error("Container creation failed : "+str(resp))
            return resp
        
    def start(self, id):
        logger.info("Starting container with ID : "+ id)  
        path = self.endpoint + str(self.startPath).format(id=id)
        response = requests.post(path)
        if(response.status_code >= 200 and response.status_code <= 299 ):
            resp =  {"status":HTTPResponses.SUCCESS, "response":str(response)}
            logger.info("Container started : " + str(resp))
            return resp
        else:    
            resp =  {"status":HTTPResponses.FAILED, "response": json.dumps(response.json())}
            logger.error("Container starting failed : "+str(resp))
            return resp




   

