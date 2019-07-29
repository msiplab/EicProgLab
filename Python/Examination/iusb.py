from abc import ABCMeta, abstractmethod

class IUsb(metaclass=ABCMeta):

	@property
	@abstractmethod
	def device_name(self):
		raise NotImplemented()
