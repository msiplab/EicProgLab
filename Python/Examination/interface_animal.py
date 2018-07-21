from abc import ABCMeta, abstractmethod
class IAnimal(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        raise NotImplemented()
    @property
    @abstractmethod
    def type(self):
        raise NotImplemented()
