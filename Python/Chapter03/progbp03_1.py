import math

class MyComplex:
    """複素数クラス"""
    
    def __init__(self, real, imag):
        """コンストラクタ"""
        # フィールド
        self.__real, self.__imag = real, imag
        
    def display(self):
        """複素数表示メソッド"""
        s = '+j' if self.__imag > 0 else '-j'
        print(str(self.__real)+s+
                str(math.fabs(self.__imag)))
            
if __name__ == '__main__':
    
    z = MyComplex(1.0,2.0)
    z.display()

    print(z.__real)
    print(z.__imag)
