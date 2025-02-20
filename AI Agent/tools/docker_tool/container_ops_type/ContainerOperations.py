from enum import Enum

'''
Operations specific to container creations, deletion, killing, getting, starting, updating. 
This constants are used to initializing the objects. These constants are mapped with "path-config.ini" files.  
'''

class ContainerOperations(Enum):
    KILL = "kill"
    CREATE = "create"
    GET = "get"
    MAIN = "containers"
    START = "start"
    REMOVE = "remove"
    UPDATE = "update"
