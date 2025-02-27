from  constants.constants import RESOURCECONSTRAINTS
import json

def getConstraintForPrompt():
    with open(RESOURCECONSTRAINTS) as data:
        temp = json.load(data)
        data.close()
    resourceConstraints = temp["resourceConstraints"]
    tempList = list(map(lambda x: {x : extractConstraintHelper(resourceConstraints[x])}, list(resourceConstraints.keys())))
    transformed = {}
    for i in tempList:
        transformed.update(i)
    return transformed

def extractConstraintHelper(constraints:list):
    tempList:list = []
    for constraint in constraints:
        try:
            tempList.append({
                "id": constraint["id"], 
                "constraint" : constraint["constraint"], 
                "description" : constraint["description"],
                "bounds": constraint["bounds"]
            })
        except KeyError:
            tempList.append({
                "id": constraint["id"], 
                "constraint" : constraint["constraint"], 
                "description" : constraint["description"]
            })
    return tempList

