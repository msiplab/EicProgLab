"""ラムダ式のサンプル"""
from random import gauss

f = lambda x: 2.0*x + gauss(0,0.01)

for n in range(10):
    x = 0.1 * n
    print('f({0: 4.3f}) ~ {1: 4.3f}'.format(x,f(x)))