public class ThreadsExample {
    public static void main(String args[]) {
	/* �X���b�h�I�u�W�F�N�g�̃C���X�^���X�� */
	CiaoThread calro = new CiaoThread("Calro",2000);
	CiaoThread maria = new CiaoThread("Maria",1000);
	
        /* �X���b�h�X�^�[�g */
        calro.start(); // run() ���T�u�X���b�g�Ƃ��Ď��s
        maria.start(); 
        try { 
            /* �X���b�h�I���ҋ@ */
            calro.join();
            maria.join();
            System.out.println("Finish!");
        } catch (InterruptedException ie) {
            System.err.println(ie.getMessage());
        }
    }
}
