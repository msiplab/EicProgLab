from iusb import IUsb
from usb_device_factory import UsbDeviceFactory

def main():
    nUsbPorts = 4
    computer = Computer(nUsbPorts)
    keyboard = UsbDeviceFactory.create_device('KB')
    mouse = UsbDeviceFactory.create_device('MOU')
    memory = UsbDeviceFactory.create_device('MEM')
    computer.plugin(memory, 0)
    computer.plugin(keyboard, 2)
    computer.plugin(mouse, 3)
    computer.display_state()
    computer.unplug(0)
    computer.display_state()

class Computer():
    def __init__(self, nPorts):
        self.__nPorts = nPorts
        self.__usbs = [ None for iPort in range(0,nPorts) ]

    def plugin(self, device, iPort):
        self.__usbs[iPort] = device

    def unplug(self, iPort):
        """  d """
        self.__usbs[iPort] = None

    def display_state(self):
        print('USB接続状況（ポート数: ' + str(self.__nPorts) + '）')
        for iPort in range(0,self.__nPorts):
           if self.__usbs[iPort] != None:
               print('{:d}: {}'.format(iPort, \
               self.__usbs[iPort].device_name),end=' ')
        print()

if __name__ == '__main__':
    main()
