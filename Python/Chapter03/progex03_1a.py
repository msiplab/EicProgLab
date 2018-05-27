"""push-down スタックの例"""
from my_stack import MyStack

STACK_SIZE = 100 # スタックサイズ

def main():
    """main関数"""
    
    mystack = MyStack(STACK_SIZE) # インスタンス化
    
    mystack.pushdown('a') # データ入力
    mystack.pushdown('b')
    mystack.pushdown('c')
    
    while( not mystack.isempty() ): # データ出力
        print( mystack.popup() )
        
if __name__ == '__main__':
    
    main()
