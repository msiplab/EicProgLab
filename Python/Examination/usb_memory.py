from iusb import IUsb

class UsbMemory(IUsb):
	
	@property
	def device_name(self):
		
		return 'メモリ'
