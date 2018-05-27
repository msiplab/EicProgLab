public class ProgEx9_5 {

    /* 定数 */
    static final int STACK_SIZE=100; // スタックサイズ 

    /* フィールド */
    static char mystack[] = new char[STACK_SIZE];
    static int top;

    public static void main(String args[]){
	initStack(); // スタック初期化 

	pushDown('a'); /* データ入力 */
	pushDown('b');
	pushDown('c');

	while( !isEmpty() ) // データ出力 
	    System.out.println(popUp());
    }

    /* スタック初期化 */
    static void initStack(){ 
	top = -1; 
    }

    /* プッシュ */
    static void pushDown(char data){ 
	    top++;
	if ( top >= STACK_SIZE ) {
	    System.err.println("stack overflow");
	    System.exit(0);
	}
	mystack[top] = data;
    }

    /* ポップ */
    static char popUp(){ 
	if (top < 0) {
	    System.err.println("popup from empty stack");
	    System.exit(0);
	}
	top--;
	return mystack[top+1];
    }

    /* 空か否か */
    static boolean isEmpty(){ 
	if (top < 0)
	    return true;
	else
	    return false;
    }

}