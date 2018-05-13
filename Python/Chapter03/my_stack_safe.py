import sys

class MyStack:
    """push-down スタッククラス"""
    
    def __init__(self, stackSize):
        """コンストラクタ（初期化）"""
        
        # フィールド
        self.__myStack = [ ' ' for i in range(stackSize) ]
        self.__top  = -1;
        
    @property
    def top(self):
        """top のゲッターメソッド"""
        return self.__top;
        
    def pushDown(self, data):
        """プッシュダウン"""
        
        self.__top += 1
        if (self.__top > len(self.__myStack)):
            print('stack overflow', file=sys.stderr)
            sys.exit(0)
            
        self.__myStack[self.__top] = data
        
    def popUp(self):
        """ポップアップ"""
        
        if (self.__top < 0):
            print('popup from empty stack', file=sys.stderr)
            sys.exit(0)
        
        self.__top -= 1
        
        return self.__myStack[self.__top+1]
        
    def isEmpty(self):
        """空か否か"""
        
        if (self.__top < 0):
            return True
        else:
            return False
