from iusb import IUsb

class UsbMouse(IUsb):
	
	@property
	def device_name(self):
		
		""" a """
		return 'マウス'
