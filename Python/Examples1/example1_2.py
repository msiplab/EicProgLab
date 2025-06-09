"""
example1_2.py
Copyright (c) 2018-2025, Shogo MURAMATSU, All rights reserved
"""
from my_complex import MyComplex
import sys
import math

def main(args):
    #引数の数の確認
    if len(args) != 5:
        print('引数の数は 4 つ必要です．')
        sys.exit(0)
        
    #コマンド引数からのデータの読み込み
    #MyComplexクラスをインスタンス化
    z0 = MyComplex(float(args[1]),float(args[2]))
    z1 = MyComplex(float(args[3]),float(args[4]))
    
    #各複素数の内容を表示して確認
    print(' z0 \t= ' + str(z0))
    print(' z1 \t= ' + str(z1))
    
    #符号反転の結果を表示
    z2 = z0.neg()
    print('-z0 \t= ' + str(z2))
    z2 = z1.neg()
    print('-z1 \t= ' + str(z2))
    
    #絶対値の結果を表示
    print('|z0| \t= ' + str(z0.abs()))
    print('|z1| \t= ' + str(z1.abs()))
    
    #２つの複素数の加算
    z2 = z0.__add__(z1) # z2 = z0 + z1 でも OK
    print('z0+z1 \t= ' + str(z2))
    
    #２つの複素数の減算
    z2 = z0.__sub__(z1) # z2 = z0 - z1 でも OK
    print('z0-z1 \t= ' + str(z2))
    
    #２つの複素数の積
    z2 = z0.__mul__(z1) # z2 = z0 * z1 でも OK
    print('z0*z1 \t= ' + str(z2))
    
if __name__ == '__main__':
    main(sys.argv)
