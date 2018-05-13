"""push-down スタックの例"""
import my_stack as ms
import top_access as ta

STACK_SIZE = 100 # スタックサイズ

def main():
    """main関数"""
    
    mystack = ms.MyStack(STACK_SIZE) # インスタンス化
    
    mystack.pushdown('a') # データ入力
    mystack.pushdown('b')
    mystack.pushdown('c')
    ta.displaytop(mystack)
    
    while( not mystack.isempty() ): # データ出力
        print( mystack.popup() )
        
if __name__ == '__main__':
    
    main()
