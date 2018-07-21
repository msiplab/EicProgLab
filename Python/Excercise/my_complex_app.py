import sys
import math

def main(args):
    '''メイン関数'''
    real = float(args[1])
    imag = float(args[2])
    print('Re(z) = {0: .2f}'.format(real))
    print('Im(z) = {0: .2f}'.format(imag))
    print('z     = ',end='')
    display(real,imag)
    print('|z|   = {0: .2f}'.format(\
    cabs(real,imag)))
    
    
def display(real,imag):
    '''表示関数'''
    s = '-' if ( imag < 0 ) else '+'
    print('{0: .2f} {1} i{2:.2f}'.format(\
    real,s,abs(imag)))


def cabs(real, imag):
    '''絶対値計算関数'''
    return math.sqrt(real*real + imag*imag)


if __name__ == '__main__':
    main(sys.argv)
