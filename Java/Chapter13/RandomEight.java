import java.util.Random;

public class RandomEight {
    static final int MAX = 8;

    public static void main(String args[]) {
        if(args.length < 1 ) {
            System.err.println("�����̐����w�肵�Ă�������");
            System.exit(0);
        }
        Random generator = new Random();
        int nSamples = Integer.parseInt(args[0]);

        for(int iSample=0; iSample<nSamples; iSample++) 
            System.out.println(generator.nextInt(MAX)+1);
    }
}
