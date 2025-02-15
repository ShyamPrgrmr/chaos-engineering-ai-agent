from enum import Enum

class ContainerOperations(Enum):
    KILL = "kill"
    CREATE = "create"
    GET = "get"
    MAIN = "containers"
    START = "start"
