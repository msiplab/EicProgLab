"""
my_complex.py
Copyright (c) 2018-2025, Shogo MURAMATSU, All rights reserved
"""
import math

class MyComplex:
    
    def __init__(self, real, imag):
        """コンストラクタ"""
        self.__real = real
        self.__imag = imag
    
    def __str__(self):
        """複素数の文字列化"""
        sgn = ' - j' if self.__imag < 0 else ' + j'
        sreal = str(float(self.__real)) 
        simag = sgn + str(math.fabs(self.__imag))
        return sreal + simag
        
    def neg(self):
        """複素数の符号反転演算"""
        return MyComplex(-self.__real, -self.__imag)
        
    def abs(self):
        """複素数の絶対値"""
        return math.sqrt(self.__real**2 + self.__imag**2)
        
    def __add__(self, another):
        """複素数の加算"""
        resreal = self.__real + another.__real
        resimag = self.__imag + another.__imag
        return MyComplex(resreal, resimag)
        
    def __sub__(self, another):
        """複素数の減算"""
        return self.__add__(another.neg())
        
    def __mul__(self, another):
        """複素数の積"""
        resreal = self.__real*another.__real \
                   - self.__imag*another.__imag
        resimag = self.__real*another.__imag \
                   + self.__imag*another.__real
        return MyComplex(resreal, resimag)

if __name__ == '__main__':
    z1 = MyComplex(1,2)
    z2 = MyComplex(3,-4)
    print(z1.abs())
    print(z2.abs())

    print("\nメソッドとして呼び出し")
    print(z1.__str__())
    print(z2.__str__())    
    print(z1.__add__(z2))
    print(z1.__sub__(z2))
    print(z1.__mul__(z2))

    # 上記メソッドは演算子をオーバライドしているため
    print("\n演算子として呼び出し")    
    print(z1)    
    print(z2)        
    print(z1 + z2)
    print(z1 - z2)
    print(z1 * z2)

    