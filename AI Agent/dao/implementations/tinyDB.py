from dao.ChatHistory import ChatHistory
from constants.Entity import Entity


class TinyDB(ChatHistory):

    def __init__(self):
        self.sessionId = super().getSessionID()

    def createChatHistory(self):
        pass

    def addIntoChatHistory(self, data:str, entity:Entity):
        
        pass
    
    #num - How many lines to fetch. 
    def getFromChatHistory(self, num:int):
        pass