"""push-down スタックの例"""
import sys

STACK_SIZE = 100 # スタックサイズ 
mystack = [ ' ' for i in range(STACK_SIZE) ]
top = int()

def main():
    """main関数"""
    
    initStack()   # スタック初期化
    
    pushDown('a') # データ入力 
    pushDown('b')
    pushDown('c')
    
    while( not isEmpty() ): # データ出力
        print(popUp())
 
def initStack():
    """スタック初期化"""
    global top
    
    top = -1
    
def pushDown(data):
    """プッシュ"""
    global top
    
    top += 1
       
    if ( top >= STACK_SIZE ):
        print('stack overflow', file=sys.stderr)
        sys.exit(0)
    
    mystack[top] = data
    
def popUp():
    """ポップ"""
    global top
    
    if (top < 0):
        print('popup from empty stack', file=sys.stderr)
        sys.exit(0)
    
    top -= 1
    
    return mystack[top+1]

def isEmpty():
    """空か否か"""
    
    if (top < 0):
        return True
    else:
        return False

if __name__ == '__main__':
    
    main()
