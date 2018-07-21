from abc import ABCMeta, abstractmethod

class IFruit(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        raise NotImplemented()
        
        
    @property
    @abstractmethod
    def taste(self):
        raise NotImplemented()
