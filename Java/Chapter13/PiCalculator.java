import java.util.Random;

public class PiCalculator {

    public static void main(String args[]) {

        Random xgenerator = new Random();
        Random ygenerator = new Random();
        int nSamples = Integer.parseInt(args[0]);
        int nInside = 0;
        double x, y;

        for(int iSample=0; iSample<nSamples; iSample++) { 
            x = xgenerator.nextDouble();
            y = ygenerator.nextDouble();
            if (Math.sqrt(x*x+y*y) <= 1.0)
                nInside++;
	}

        System.out.println("ƒÎ ` "  + (4.0*nInside)/nSamples);
    }

}
