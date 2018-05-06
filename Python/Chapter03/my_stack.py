import sys

class MyStack:
	'''push-down スタッククラス'''
	
	def __init__(self, stackSize):
		'''コンストラクタ（初期化）'''
		
		# フィールド
		self.myStack = [ ' ' for i in range(stackSize) ]
		self.top  = -1;
		
	def pushDown(self, data):
		'''プッシュダウン'''
		
		self.top += 1
		if (self.top > len(self.myStack)):
			print('stack overflow', file=sys.stderr)
			sys.exit(0)
			
		self.myStack[self.top] = data
		
	def popUp(self):
		'''ポップアップ'''
		
		if (self.top < 0):
			print('popup from empty stack', file=sys.stderr)
			sys.exit(0)
		
		self.top -= 1
		
		return self.myStack[self.top+1]
		
	def isEmpty(self):
		'''空か否か'''
		
		if (self.top < 0):
			return True
		else:
			return False

