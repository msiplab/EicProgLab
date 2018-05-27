public class ProgEx9_5 {

    /* �萔 */
    static final int STACK_SIZE=100; // �X�^�b�N�T�C�Y 

    /* �t�B�[���h */
    static char mystack[] = new char[STACK_SIZE];
    static int top;

    public static void main(String args[]){
	initStack(); // �X�^�b�N������ 

	pushDown('a'); /* �f�[�^���� */
	pushDown('b');
	pushDown('c');

	while( !isEmpty() ) // �f�[�^�o�� 
	    System.out.println(popUp());
    }

    /* �X�^�b�N������ */
    static void initStack(){ 
	top = -1; 
    }

    /* �v�b�V�� */
    static void pushDown(char data){ 
	    top++;
	if ( top >= STACK_SIZE ) {
	    System.err.println("stack overflow");
	    System.exit(0);
	}
	mystack[top] = data;
    }

    /* �|�b�v */
    static char popUp(){ 
	if (top < 0) {
	    System.err.println("popup from empty stack");
	    System.exit(0);
	}
	top--;
	return mystack[top+1];
    }

    /* �󂩔ۂ� */
    static boolean isEmpty(){ 
	if (top < 0)
	    return true;
	else
	    return false;
    }

}