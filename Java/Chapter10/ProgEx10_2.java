public class ProgEx10_2 {

    /* �X�^�b�N�T�C�Y  */
    static final int STACK_SIZE=100;

    public static void main(String args[]){

        /* �X�^�b�N������ */
	MyStack myStack = new MyStack(STACK_SIZE);

	/* �f�[�^���� */
	for(int index=0; index<args[0].length(); index++)
	    myStack.pushDown((args[0]).charAt(index));

	/* �f�[�^�o�� */
	while( !myStack.isEmpty() )
	    System.out.print(myStack.popUp());
	System.out.println();
    }

}
