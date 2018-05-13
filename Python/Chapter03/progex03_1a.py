"""push-down スタックの例"""
import my_stack as ms

STACK_SIZE = 100 # スタックサイズ

def main():
    """main関数"""
    
    myStack = ms.MyStack(STACK_SIZE) # インスタンス化
    
    myStack.pushDown('a') # データ入力
    myStack.pushDown('b')
    myStack.pushDown('c')
    
    while( not myStack.isEmpty() ): # データ出力
        print( myStack.popUp() )
        
if __name__ == '__main__':
    
    main()
