import math

class MyComplex:
    """複素数クラス"""
    # フィールド（初期値）
    real = 0.0
    imag = 0.0
    
    '''
    def __init__(self, real, imag):
        """コンストラクタ"""
        # フィールドの初期化（クラス直下同名フィールドをコメントアウト）
        self.real, self.imag = real, imag
    '''
    
    '''
    def display(self):
        """複素数表示メソッド"""
        s = '+j' if self.imag > 0 else '-j'
        print(str(self.real)+s+str(math.fabs(self.imag)))
    '''

    '''
    def cabs(self):
        """絶対値メソッド"""

        return math.sqrt(self.real**2 + self.imag**2)
    '''
