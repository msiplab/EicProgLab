'''フィールドの例'''
import math

class MyVector:
	'''ベクトルクラス'''
	
	def __init__(self,x,y,z):
		'''初期化メソッド（コンストラクタ）'''
		self._x, self._y, self._z = x, y, z

		
	def norm(self):
		'''ノルムの計算'''
		x, y, z = self._x, self._y, self._z
		
		# 自乗和の平方根		
		return math.sqrt(x**2 + y**2 + z**2) 

if __name__ == '__main__':
	
	import fieldexample as fe
	
	vector = fe.MyVector(1., 2., 3.)
	
	print(vector.norm())
		
