public class RunnableExample {
    public static void main(String args[]) {
        /* Runnable オブジェクトのインスタンス化 */
	CiaoRunnable ciaoCalro = new CiaoRunnable("Calro",2000);
	CiaoRunnable ciaoMaria = new CiaoRunnable("Maria",1000);
	
        /* スレッドオブジェクトのインスタンス化 */
        Thread calro = new Thread(ciaoCalro);
        Thread maria = new Thread(ciaoMaria);
	
        /* スレッドスタート */
        calro.start(); // run() をサブスレッドとして実行
        maria.start(); 
        try { 
            /* スレッド終了待機 */
            calro.join();
            maria.join();
            System.out.println("Finish!");
        } catch (InterruptedException ie) {
            System.err.println(ie.getMessage());
        }
    }
}
