from enum import Enum

class Entity(Enum):
    AI = "AI"
    TOOL = "TOOL"

class EntityType(Enum):
    DOCKERTOOL = "DockerTool"
    HOSTTOOL = "HostTool"
    PROMTOOL = "PrometheusTool"
    JMETER = "JMeterTool"

class DockerToolOPS(Enum):
    CREATE = "CreateContainer"
    UPDATE = "UpdateContainer"
    KILL = "KillContainer"

