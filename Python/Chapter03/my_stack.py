import sys

class MyStack:
    """push-down スタッククラス"""
    
    def __init__(self, stacksize):
        """コンストラクタ（初期化）"""
        
        # フィールド
        self.mystack = [ ' ' for i in range(stacksize) ]
        self.top  = -1;
        
    def pushdown(self, data):
        """プッシュダウン"""
        
        self.top += 1
        if (self.top > len(self.mystack)):
            print('stack overflow', file=sys.stderr)
            sys.exit(0)
            
        self.mystack[self.top] = data
        
    def popup(self):
        """ポップアップ"""
        
        if (self.top < 0):
            print('popup from empty stack', file=sys.stderr)
            sys.exit(0)
        
        self.top -= 1
        
        return self.mystack[self.top+1]
        
    def isempty(self):
        """空か否か"""
        
        if (self.top < 0):
            return True
        else:
            return False

