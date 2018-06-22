import sys
import numpy as np
from scipy import optimize

def main(args):
    # 初期値
    x0 = float(args[1])
    # ニュートン法
    root = optimize.newton(f, x0, df)
    # 解の表示
    print(root)

def f(x):
    return 0.5 - x + 0.2 * np.sin(x)
    
def df(x):
    return  -1 + 0.2 * np.cos(x)

if __name__ == '__main__':
    main(sys.argv)
