from abc import ABCMeta, abstractmethod

class IThreeDimensionalObject(metaclass=ABCMeta):  
    
    @abstractmethod
    def isinside(self,x,y,z):
               raise NotImplemented()
        
    @property
    @abstractmethod
    def name(self):
        raise NotImplemented()    
    
    @property
    @abstractmethod
    def analyticalsolution(self):
        raise NotImplemented()
