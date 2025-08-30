from abc import ABC,abstractmethod

class car(ABC):
    
    @abstractmethod
    def color(self,attribute):
        pass
    
    @abstractmethod
    def brand(self,attribute2):
        pass
    
