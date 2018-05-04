'''正三角形の面積を求めるプログラム
'''
import sys

# ルート3の定義
SQRT_OF_3 = 1.73205080756888

def main(args):
	# 引数の数
	nArgs = len(args)-1
	if nArgs != 1:
		print('エラー:引数の数 ',nArgs)
	else:
		# コマンド引数からのデータの読み込み（C言語の atof に相当）
		ell = float(args[1])
		
		# 面積の計算(底辺×高さ/2) 
		area = ell * (SQRT_OF_3 / 2.0 * ell) / 2.0
		
		# 正三角形の面積の表示 
		print('一辺の長さが ',ell,' の正三角形の面積')
		print('     = ',area)
	
	return 0

     
if __name__ == '__main__':
	
	main(sys.argv)
