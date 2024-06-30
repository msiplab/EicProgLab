from abc import ABCMeta, abstractmethod

class IThreeDimensionalObject(metaclass=ABCMeta):  
    
    @abstractmethod
    def is_inside(self,x,y,z):
        raise NotImplemented()
        
    @property
    @abstractmethod
    def name(self):
        raise NotImplemented()    
    
    @property
    @abstractmethod
    def analytical_solution(self):
        raise NotImplemented()
