from digital_tv import DigitalTv
from digital_tv_3d import DigitalTv3d

def main():
    region = '新潟'
    for flag in [ True, False]:
        if flag == True:
            digitaltv = DigitalTv3d(region)
        else:
            digitaltv = DigitalTv(region)
        digitaltv.display(8)

if __name__ == '__main__':
    main()
