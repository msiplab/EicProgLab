import math

class MyComplex:
	'''複素数クラス'''
	
	# フィールド
	real = float()
	imag = float()
	
	def display(self):
		'''複素数表示メソッド'''
		
		s = '+j' if self.imag > 0 else '-j'
		print(str(self.real)+s+str(math.fabs(self.imag)))

