import java.util.Random;

public class PiRunnable implements Runnable {

    private int id, nSamples;
    private Random xgenerator = new Random();
    private Random ygenerator = new Random();
    
    PiRunnable(int id, int nSamples) {
	this.id = id;
	this.nSamples = nSamples;
    }
    
    public void run() {
	int nInside = 0;
	double x, y;
        for(int iSample=0; iSample<this.nSamples; iSample++) { 
            x = this.xgenerator.nextDouble();
            y = this.ygenerator.nextDouble();
            if (Math.sqrt(x*x+y*y) <= 1.0)
                nInside++;
	} 
        System.out.println(this.id + " : ƒÎ ` "  + 
			   (4.0*nInside)/this.nSamples); 
    }
}
