import sys
import my_stack_safe as ms

STACK_SIZE = 100

def main(args):
    # スタック初期化
    myStack = ms.MyStack(STACK_SIZE)
    
    # データ入力
    for index in range(len(args[1])):
        myStack.pushDown(args[1][index])
    
    # データ出力
    while( not myStack.isEmpty() ):
        print(myStack.popUp(), end='')
    print()

if __name__ == '__main__':
    
    main(sys.argv)
    
      
