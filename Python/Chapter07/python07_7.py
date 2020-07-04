"""デコレータのサンプル"""
from random import gauss

def noisy(func):
    def noisy_func(*args, **kwargs):
        y = func(*args, **kwargs) + gauss(0,0.01)
        return y
    return noisy_func

@noisy
def f(x):
    return 2.0*x

for n in range(10):
    x = 0.1 * n
    print('f({0: 4.3f}) ~ {1: 4.3f}'.format(x,f(x)))