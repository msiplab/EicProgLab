'''フィールドの例'''
import math

class MyVector:
	'''ベクトルクラス'''
	
	def __init__(self,x,y,z):
		'''初期化メソッド（コンストラクタ）'''
		self.x, self.y, self.z = x, y, z

		
	def norm(self):
		'''ノルムの計算'''
		x, y, z = self.x, self.y, self.z
		
		# 自乗和の平方根		
		return math.sqrt(x**2 + y**2 + z**2) 

if __name__ == '__main__':
	
	import field_example as fe
	
	vector = fe.MyVector(1., 2., 3.)
	
	print(vector.norm())
		
