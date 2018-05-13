class CiaoMondo:
    """CiaoMondoクラス"""	
	
    def greet(self):
        """あいさつメソッド"""
        print('Ciao Mondo!')
	
if __name__ == '__main__':
	
	import ciao_mondo
	 as cm
	
	ciao = cm.CiaoMondo()
	
	print(ciao.__doc__)
	
	print(ciao.greet.__doc__)
	
	ciao.greet()
