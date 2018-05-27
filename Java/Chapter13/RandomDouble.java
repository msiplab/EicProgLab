import java.util.Random;

public class RandomDouble {
    public static void main(String args[]) {
	if(args.length < 1 ) {
	    System.err.println("—”‚Ì”‚ðŽw’è‚µ‚Ä‚­‚¾‚³‚¢");
	    System.exit(0);
	}
	Random generator = new Random();
        int nSamples = Integer.parseInt(args[0]);
        for(int iSample=0; iSample<nSamples; iSample++) {
            generator.setSeed(iSample);
            System.out.println(generator.nextDouble());
        }
    }
}
