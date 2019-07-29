from usb_memory import UsbMemory
from usb_keyboard import UsbKeyBoard
from usb_mouse import UsbMouse

class UsbDeviceFactory:
	
	@classmethod
	def create_device(cls,device_name):
		if device_name == 'MEM':
			
			device = UsbMemory()
			
		elif device_name == 'KB':
			
			""" b """
			device = UsbKeyBoard()
			
		elif device_name == 'MOU':
			
			device = UsbMouse()
			
		else:
			
			device = None
			
		""" c """
		return device
