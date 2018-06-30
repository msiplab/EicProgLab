import unittest
from my_complex import MyComplex

class TestMyComplex(unittest.TestCase):

    def testAdd(self):
        """加算テスト"""
        # インスタンス化
        z0 = MyComplex(1.0, 2.0)
        z1 = MyComplex(3.0, 4.0)
        # 加算の実行
        z2 = z0.add(z1)
        # 期待値
        realExpctd = 4.0
        imagExpctd = 6.0
        # 実測値
        realActual = z2.real
        imagActual = z2.imag
        # 評価
        self.assertEqual(realActual, realExpctd)
        self.assertEqual(imagActual, imagExpctd)
        
    '''
    def testSub(self):
        """減算テスト"""
        # インスタンス化
        z0 = MyComplex(1.0, 2.0)
        z1 = MyComplex(3.0, 4.0)
        # 減算の実行
        z2 = z0.sub(z1)
        # 期待値
        realExpctd = -2.0
        imagExpctd = -2.0
        # 実測値
        realActual = z2.real
        imagActual = z2.imag
        # 評価
        self.assertEqual(realActual, realExpctd)
        self.assertEqual(imagActual, imagExpctd)
    '''
        

if __name__ == '__main__':
    unittest.main()
