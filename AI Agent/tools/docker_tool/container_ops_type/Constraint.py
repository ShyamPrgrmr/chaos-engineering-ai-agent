
class Constraint:
    def __init__(self, id:str, name:str, description:str, value:str, datatype:str):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__value=value
        self.__datatype = datatype
    
    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description
    
    def getValue(self):
        return self.__value
    
    def getDataType(self):
        return self.__datatype
    
    def __str__(self):
        return f"[id: {self.__id}, name: {self.__name}, description: {self.__description}, value: {self.__value}, datatype: {self.__datatype}]"