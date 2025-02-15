import requests
import json
from constants.httpresponses import HTTPResponses


class CreateContainer():
    def __init__(self, endpoint, createPath, startPath):
        self.path = createPath
        self.startPath = startPath
        self.endpoint = endpoint
        
    def create(self, request):
        response = requests.post(self.endpoint+self.path+"?name="+request.name, json=json.loads(request.getJson()), headers={"content-type":"application/json"}) 
        if(response.status_code >= 200 and response.status_code <= 299 ):
            temp = json.dumps(response.json())
            data = json.loads(temp)
            return {"status":HTTPResponses.SUCCESS, "response":data, "id": data["Id"]}
        else:
            return {"status":HTTPResponses.FAILED, "response": json.dumps(response.json())}

    def start(self, id):
        path = self.endpoint + str(self.startPath).format(id=id)
        print(path)




   

