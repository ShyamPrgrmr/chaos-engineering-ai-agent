import json
from pathlib import Path
from typing import List

from .Constraint import Constraint
from  constants.constants import RESOURCECONSTRAINTS
from common.logger import logger 

class UpdateContainerRequest:
    def __init__(self):
        self.constraints:List[Constraint] = []
        self.resourceConstraints = self.__initResourceConstraints()

    def __initResourceConstraints(self):
        with open(RESOURCECONSTRAINTS) as data:
            resourceConstraints = json.load(data)
            data.close()
        return resourceConstraints["resourceConstraints"]
        
    def getSelectedConstraints(self):
        return self.constraints

    def addConstraint(self, id:str, value:str):
        if "cpu" in id:
            cpu = self.resourceConstraints["cpu"]
            temp = list(filter(lambda x: id==x["id"], cpu))[0]
            constraint = Constraint(id, temp["constraint"], temp["description"], value, temp["datatype"])
            self.constraints.append(constraint)

        elif "memory" in id:
            memory = self.resourceConstraints["memory"]
            temp = list(filter(lambda x: id==x["id"], memory))[0]
            constraint = Constraint(id, temp["constraint"], temp["description"], value, temp["datatype"])
            self.constraints.append(constraint)

        else:
            logger.error(f"ID - {id} not matching with any constraint.")
        
        return self

    def build(self):
        request = {}

        if(len(self.constraints)==0):
            logger.error(f"No constraints added to update : {constraint}.")

        for constraint in self.constraints:
            if("integer" in constraint.getDataType() ):
                val = int(constraint.getValue())
            else:
                val = str(constraint.getValue())
            request.update({
                constraint.getName() : val
            })

        return json.dumps(request)

if __name__ == "__main__":
    UpdateContainerRequest()





