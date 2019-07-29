import sys
import math

# メイン関数
def main(args):
	EPS = 1e-2 # 誤差の許容値
	count = 0 # 繰返し回数
	ycur = 1.0 # 出力

	global x		
	x = float(args[1]) # 入力
	
	# 初期値の表示
	print('{:3d}: y = {:6.3f}'.format(count,ycur))
	
	# 繰返し計算
	while True:
		count += 1 # カウントアップ
		ypre = ycur # 更新前の値の保存
		ycur = update(ypre) # 値の更新
		# 更新値の表示
		print('{:3d}: y = {:6.3f}'.format(count,ycur))
		if math.fabs(ycur-ypre)<EPS: # 収束判定
			break

# 更新関数
def update(y):
	global x
	y = ( y + (x/y) ) / 2.0 # 値の更新
	return y

if __name__ == '__main__':
	main(sys.argv)
