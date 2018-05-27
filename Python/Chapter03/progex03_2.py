import sys
from my_stack_safe import MyStack

STACK_SIZE = 100

def main(args):
    # スタック初期化
    mystack = MyStack(STACK_SIZE)
    
    # データ入力
    for index in range(len(args[1])):
        mystack.pushdown(args[1][index])
    
    # データ出力
    while( not mystack.isempty() ):
        print(mystack.popup(), end='')
    print()

if __name__ == '__main__':
    
    main(sys.argv)
    
      
