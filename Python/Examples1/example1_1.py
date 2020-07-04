"""
example1_1.py
(c) Copyright 2018-2020, Shogo MURAMATSU, All rights reserved
"""
import sys

SQRT_OF_3 = 1.73205080756888

def main(args):
    if len(args) != 2:
        print('エラー：引数の数' + str(len(args)))
    else:
        # 一辺の長さ
        ell = float(args[1])
        # 面積の計算（底辺×高さ/2）
        area = ell * (SQRT_OF_3/2.0 * ell)/2.0
        # 正三角形の面積の表示
        print('一辺の長さが' + str(ell) + 'の正三角形の面積')
        print('    = ' + str(area))

if __name__ == '__main__':
    main(sys.argv)
        
        
