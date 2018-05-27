public class ProgEx10_1a {

    /* 定数 */
    static final int STACK_SIZE=100; // スタックサイズ 

    public static void main(String args[]){
	MyStack myStack = new MyStack(STACK_SIZE); // スタック初期化 

	myStack.pushDown('a'); /* データ入力 */
	myStack.pushDown('b');
	myStack.pushDown('c');

	while( !myStack.isEmpty() ) // データ出力 
	    System.out.println(myStack.popUp());
    }

}
