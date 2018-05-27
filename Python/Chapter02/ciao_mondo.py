class CiaoMondo:
    """CiaoMondoクラス"""	
	
    def greet(self):
        """あいさつメソッド"""
        print('Ciao Mondo!')
	
if __name__ == '__main__':
	
	from ciao_mondo import CiaoMondo
	
	ciao = CiaoMondo()
	
	print(ciao.__doc__)
	
	print(ciao.greet.__doc__)
	
	ciao.greet()
