from abc import ABCMeta, abstractmethod

class IProbabilityDensityFunction(metaclass=ABCMeta):  
    
    @abstractmethod
    def parameter_inquiry(self):
        raise NotImplemented()
             
    @abstractmethod
    def draw_sample(self):
        raise NotImplemented()
        
    @property
    @abstractmethod
    def name(self):
        raise NotImplemented()    
    
    @property
    @abstractmethod
    def analytical_expectation(self):
        raise NotImplemented()
