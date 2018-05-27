public class PiThreadCalculator {
    public static void main(String args[]) {
	
        int nThreads = Integer.parseInt(args[0]);;
        int nSamples = Integer.parseInt(args[1]);
        Thread[] threads = new Thread[nThreads];
	
        for(int iThread = 0; iThread < nThreads; iThread++){
            PiRunnable piRunnable= 
		new PiRunnable(iThread,nSamples);
	    
            threads[iThread] = new Thread(piRunnable);
	    
            /* スレッドスタート */ 
            threads[iThread].start(); 
	}
	
	try { 
	    for(int iThread = 0; iThread < nThreads; iThread++){
                threads[iThread].join(); /* スレッド終了待機 */
	    }
	    System.out.println("Finish!");
	} catch (InterruptedException ie) {
            System.err.println(ie.getMessage());
	}
    }
}
