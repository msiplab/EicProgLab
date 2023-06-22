from random import random

class VolumeEstimator:
    
    def __init__(self,object3d,nSamples):
        """コンストラクタ"""
        self.__object3d = object3d
        self.__nSamples = nSamples
    
    def run(self):
        """体積の推定"""
        # サンプル数の取得
        nSamples = self.__nSamples
        # 単位円内のサンプル数
        nInside = 0
        # 擬似乱数の生成と評価
        for iSample in range(nSamples):
            x = 2.0*(random()-0.5) # [-1,1]
            y = 2.0*(random()-0.5) # [-1,1]
            z = 2.0*(random()-0.5) # [-1,1]
            if self.__object3d.is_inside(x,y,z):
                nInside += 1
        return (8.0*nInside)/nSamples

