import math

def main():
    real = math.sqrt(3.0)/2.0
    imag = 0.5
    angle = math.atan2(imag, real)*180.0/math.pi
    print(angle)

if __name__ == '__main__':

    main()
