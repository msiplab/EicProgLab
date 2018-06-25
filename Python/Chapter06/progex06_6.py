import sys
import math
import matplotlib.pyplot as plt
from random import random

def main(args):
    
    try:
        # サンプル数の取得
        nSamples = int(args[1])
        # 単位円内のサンプル数
        nInside = 0
        # 擬似乱数の生成と評価
        xin, yin  = [], []
        xout, yout = [], []
        for iSample in range(nSamples):
            x = random()
            y = random()
            if math.sqrt(x**2 + y**2) < 1.0:
                nInside += 1
                xin.append(x)
                yin.append(y)
            else:
                xout.append(x)
                yout.append(y)
        res = (4.0*nInside)/nSamples
        print('π 〜 {0} (N={1})'.format(res,nSamples))
        # 散布図
        plt.scatter(xin,yin,c='blue',marker='o',label='inside')
        plt.scatter(xout,yout,c='red',marker='x',label='outside')
        plt.xlim(0.0,1.0)
        plt.ylim(0.0,1.0)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('$\pi \simeq$ {0} (N={1})'.format(res,nSamples))
        plt.legend(loc='lower left')
        plt.axes().set_aspect('equal')
        plt.show()
    except IndexError as ie:
        print('引数の数が足りません', file=sys.stderr)
        
if __name__ == '__main__':
    main(sys.argv)
