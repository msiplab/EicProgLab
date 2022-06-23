"""
example1_1.py
(c) Copyright 2022, Shogo MURAMATSU, All rights reserved
"""
import sys

# 電源電圧値
SRC_VOLTAGE = 5.0
# 抵抗の数
NUM_REGS = 5

def main(args):
    if len(args) != 6:
        print('エラー：引数の数' + str(len(args)))
    else:
        # 抵抗値 Ri
        r = [ 0.0 for idx in range(NUM_REGS) ]
        for idx in range(NUM_REGS):
            r[idx] = float(args[idx+1])
        # 抵抗R0にかかる電圧V
        v0 = (r[2]*r[3]-r[1]*r[4])*r[0]*SRC_VOLTAGE / \
            ( r[1]*r[3]*(r[2]+r[4]) + \
              r[2]*r[4]*(r[1]+r[3]) + \
              r[0]*(r[1]+r[3])*(r[2]+r[4]) )            
        # 電圧Vの表示
        print('電源電圧 E = ' + str(SRC_VOLTAGE) + ' V')
        for idx in range(NUM_REGS):
            print('抵抗 R' + str(idx) + ' = ' + str(r[idx]) + ' Ω')
        print('電圧 V0 = ' + str(v0) + ' V')

if __name__ == '__main__':
    main(sys.argv)
        
        
