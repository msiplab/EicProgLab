public class MyStack {

    /* �t�B�[���h */
    private char[] _myStack;
    private int _top;

    /* �R���X�g���N�^�i�������j*/
    public MyStack(int stackSize){
	_myStack = new char[stackSize];
	_top = -1;
    }

    public void pushDown(char data){
	_top++;
	if (_top >= _myStack.length) {
	    System.err.println("stack overflow");
	    System.exit(0);
	}
	_myStack[_top] = data;
    }	

    public char popUp(){
	if (_top < 0) {
	    System.err.println("popup from empty stack");
	    System.exit(0);
	}
	_top--;
	return _myStack[_top+1];
    }

    public boolean isEmpty(){
	if (_top < 0)
	    return true;
	else
	    return false;
    }

    public int getTop() {
	return this._top;
    }

}
