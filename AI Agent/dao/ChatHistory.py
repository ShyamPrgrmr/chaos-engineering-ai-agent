from abc import ABC, abstractmethod
import random, string

class ChatHistory(ABC):

    def getSessionID(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


    @abstractmethod
    def createChatHistory(self):
        pass
    @abstractmethod
    def addIntoChatHistory(self, data):
        pass
    @abstractmethod
    def getFromChatHistory(self):
        pass
    