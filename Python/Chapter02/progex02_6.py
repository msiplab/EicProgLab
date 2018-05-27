"""インスタンス化の例"""
from my_complex import MyComplex 
import math
import sys

def main(args):
	"""main関数"""
	z1 = MyComplex()
	z2 = MyComplex()
	
	z1.real, z1.imag = float(args[1]), float(args[2])
	z2.real, z2.imag = float(args[3]), float(args[4])
	
	# インスタンスメソッドの呼び出し
	z1.display()
	z2.display()

if __name__ == '__main__':
	
	main(sys.argv)
	
