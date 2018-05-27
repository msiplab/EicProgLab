"""インスタンス化の例"""
from my_complex import MyComplex
import math
import sys

def main(args):
    """main関数"""
    z = MyComplex()
    
    z.real, z.imag = float(args[1]), float(args[2])
    
    display(z)


def display(z):
    """複素数表示関数"""
    
    s = '+j' if z.imag > 0 else '-j'
    print(str(z.real)+s+str(math.fabs(z.imag)))

if __name__ == '__main__':
    
    main(sys.argv)
