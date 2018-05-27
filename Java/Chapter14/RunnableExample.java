public class RunnableExample {
    public static void main(String args[]) {
        /* Runnable �I�u�W�F�N�g�̃C���X�^���X�� */
	CiaoRunnable ciaoCalro = new CiaoRunnable("Calro",2000);
	CiaoRunnable ciaoMaria = new CiaoRunnable("Maria",1000);
	
        /* �X���b�h�I�u�W�F�N�g�̃C���X�^���X�� */
        Thread calro = new Thread(ciaoCalro);
        Thread maria = new Thread(ciaoMaria);
	
        /* �X���b�h�X�^�[�g */
        calro.start(); // run() ���T�u�X���b�h�Ƃ��Ď��s
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
