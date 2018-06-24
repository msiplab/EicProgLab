import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def main():
    e = 1.0 # E = 1.0[V] 
    r = 1.0e3 # R = 1.0[kΩ]
    ell = 50.0e-3 # L = 50.0 [mH]
    c = 0.1e-6 # C = 0.1[μF]
    ts = 0.0 # 0.0[ms] 開始時刻  
    te = 1.0e-3 # 1.0[ms] 終了時刻 
    v0 = [ 0.0, 0.0 ] # v = 0.0[V], dv/dt = 0.0 [V/s] 初期条件
    h = 1.0e-5 # ステップ
    t = np.arange(ts, te, h) 
    
    # 計算の実行と標準出力
    zeta = r * c / (2 * np.sqrt( ell * c ) )
    x = t / np.sqrt(ell * c) # x の設定
    y0 = np.array( v0 ) / e # y, dy/dx の初期値設定
        
    # 数値積分
    y = odeint(f, y0, x, args = ( zeta, ) )
    v = e * y;
    
    # グラフ描画
    plt.plot(t,v[:,0])
    plt.title('Transient response ($\zeta$={0})'.format(zeta))
    plt.xlabel('$t$ [s]')
    plt.ylabel('$v(t)$ [V]')
    plt.grid()
    plt.show()
        
def f(y,x,zeta):
    return [ 
                y[1],
                -y[0]-2*zeta*y[1] + 1
            ]

if __name__ == '__main__':
    main()

