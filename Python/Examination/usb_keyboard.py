from iusb import IUsb

class UsbKeyBoard(IUsb):
	
	@property
	def device_name(self):
		
		return 'キーボード'
