from random import random

class ExpectationEstimator:
    
    def __init__(self,pdf,nSamples):
        """コンストラクタ"""
        self.__pdf = pdf
        self.__nSamples = nSamples
    
    def run(self):
        """期待値の推定"""
        # サンプル数の取得
        nSamples = self.__nSamples
        # 累積加算値の初期化
        acc = 0.0
        # 擬似乱数の生成と評価
        for iSample in range(nSamples):
            x = self.__pdf.draw_sample()
            acc += x  
        return acc/nSamples
    

