public class MyStack {

    /* �t�B�[���h */
    char[] myStack;
    int top;

    /* �R���X�g���N�^�i�������j*/
    public MyStack(int stackSize){
	myStack = new char[stackSize];
	top = -1;
    }

    public void pushDown(char data){
	top++;
	if (top >= myStack.length) {
	    System.err.println("stack overflow");
	    System.exit(0);
	}
	myStack[top] = data;
    }	

    public char popUp(){
	if (top < 0) {
	    System.err.println("popup from empty stack");
	    System.exit(0);
	}
	top--;
	return myStack[top+1];
    }

    public boolean isEmpty(){
	if (top < 0)
	    return true;
	else
	    return false;
    }


}
