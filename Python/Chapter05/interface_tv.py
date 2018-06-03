from abc import ABCMeta, abstractmethod

class ITv(metaclass=ABCMeta):  
    
    
    @abstractmethod
    def display(self,channel):
        raise NotImplemented()

        
    @property
    @abstractmethod
    def region(self):
        raise NotImplemented()
        
    
    @region.setter
    @abstractmethod
    def region(self, value):
        raise NotImplemented()
