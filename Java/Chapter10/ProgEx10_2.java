public class ProgEx10_2 {

    /* スタックサイズ  */
    static final int STACK_SIZE=100;

    public static void main(String args[]){

        /* スタック初期化 */
	MyStack myStack = new MyStack(STACK_SIZE);

	/* データ入力 */
	for(int index=0; index<args[0].length(); index++)
	    myStack.pushDown((args[0]).charAt(index));

	/* データ出力 */
	while( !myStack.isEmpty() )
	    System.out.print(myStack.popUp());
	System.out.println();
    }

}
