from digital_tv import DigitalTv
from digital_tv_3d import DigitalTv3d

def main():
	
	# 基底クラス
    tv = DigitalTv('新潟')
    tv.display(8)
    
    # 派生クラス
    tv3d = DigitalTv3d('新潟')
    tv3d.is3d = False
    tv3d.display(8)
    tv3d.is3d = True
    tv3d.display(8)
    
if __name__ == '__main__':
	main()
