public class PiThreadCalculator {
    public static void main(String args[]) {
	
        int nThreads = Integer.parseInt(args[0]);;
        int nSamples = Integer.parseInt(args[1]);
        Thread[] threads = new Thread[nThreads];
	
        for(int iThread = 0; iThread < nThreads; iThread++){
            PiRunnable piRunnable= 
		new PiRunnable(iThread,nSamples);
	    
            threads[iThread] = new Thread(piRunnable);
	    
            /* �X���b�h�X�^�[�g */ 
            threads[iThread].start(); 
	}
	
	try { 
	    for(int iThread = 0; iThread < nThreads; iThread++){
                threads[iThread].join(); /* �X���b�h�I���ҋ@ */
	    }
	    System.out.println("Finish!");
	} catch (InterruptedException ie) {
            System.err.println(ie.getMessage());
	}
    }
}
