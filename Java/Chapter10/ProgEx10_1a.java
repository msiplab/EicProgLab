public class ProgEx10_1a {

    /* �萔 */
    static final int STACK_SIZE=100; // �X�^�b�N�T�C�Y 

    public static void main(String args[]){
	MyStack myStack = new MyStack(STACK_SIZE); // �X�^�b�N������ 

	myStack.pushDown('a'); /* �f�[�^���� */
	myStack.pushDown('b');
	myStack.pushDown('c');

	while( !myStack.isEmpty() ) // �f�[�^�o�� 
	    System.out.println(myStack.popUp());
    }

}
