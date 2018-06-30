import sys
import time
import math
from random import random
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed

def main(args):
    nProcess = int(args[1]) if len(args) > 1 else 5
    nSamples = int(args[2]) if len(args) > 2 else 100    
    print('プロセス数：{0}'.format(nProcess))
    print('プロセス毎のサンプル数：{0}'.format(nSamples))
    print('総サンプル数：{0}'.format(nProcess*nSamples))
    
    # 開始時刻
    start_time = time.time()
    # サブプロセス実行用オブジェクトのインスタンス化
    piest = [ PiEstimator(nSamples) for id in range(nProcess) ]
    piacc = 0.0
    with ProcessPoolExecutor() as executor:
        # サブプロセスのスタートと ID の割り当て
        future_piest = { executor.submit(piest[id].run) : 
                                id for id in range(nProcess) }
        # サブプロセスの結果の回収
        for future in as_completed(future_piest):
            id = future_piest[future]
            pires = future.result()
            print('{0:02d}: {1:6.4f}'.format(id,pires))
            piacc += pires
    # 推定の平均値
    piave = piacc/nProcess
    # 処理時間
    elapsed_time = time.time() - start_time
    # 結果表示
    print('平均値： {0:6.4f}'.format(piave))
    print('処理時間： {0:6.4f} [s]'.format(elapsed_time))
    
class PiEstimator:
    
    def __init__(self,nSamples):
        """コンストラクタ"""
        self.__nSamples = nSamples
        
    
    def run(self):
        """円周率の推定"""
        # サンプル数の取得
        nSamples = self.__nSamples
        # 単位円内のサンプル数
        nInside = 0
        # 擬似乱数の生成と評価
        for iSample in range(nSamples):
            x = random()
            y = random()
            if math.sqrt(x**2 + y**2) < 1.0:
                nInside += 1       
        return (4.0*nInside)/nSamples

if __name__ == '__main__':
    main(sys.argv)
