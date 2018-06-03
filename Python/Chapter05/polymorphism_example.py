from digital_tv import DigitalTv
from digital_tv_3d import DigitalTv3d

if __name__ == '__main__':
    region = '新潟'
    digitaltv = DigitalTv(region)
    digitaltv.display(8)
    
    digitaltv = DigitalTv3d(region)
    digitaltv.display(8)
