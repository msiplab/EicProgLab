import sys

class MyStack:
    """push-down スタッククラス"""
    
    def __init__(self, stacksize):
        """コンストラクタ（初期化）"""
        
        # フィールド
        self.__mystack = [ ' ' for i in range(stacksize) ]
        self.__top  = -1;
        
    @property
    def top(self):
        """top のゲッターメソッド"""
        return self.__top;
        
    def pushdown(self, data):
        """プッシュダウン"""
        
        self.__top += 1
        if (self.__top > len(self.__mystack)):
            print('stack overflow', file=sys.stderr)
            sys.exit(0)
            
        self.__mystack[self.__top] = data
        
    def popup(self):
        """ポップアップ"""
        
        if (self.__top < 0):
            print('popup from empty stack', file=sys.stderr)
            sys.exit(0)
        
        self.__top -= 1
        
        return self.__mystack[self.__top+1]
        
    def isempty(self):
        """空か否か"""
        
        if (self.__top < 0):
            return True
        else:
            return False
