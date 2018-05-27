public class ThreadsExample {
    public static void main(String args[]) {
	/* スレッドオブジェクトのインスタンス化 */
	CiaoThread calro = new CiaoThread("Calro",2000);
	CiaoThread maria = new CiaoThread("Maria",1000);
	
        /* スレッドスタート */
        calro.start(); // run() をサブスレットとして実行
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
