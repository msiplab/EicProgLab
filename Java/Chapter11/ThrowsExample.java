public class ThrowsExample {
    
    public static void main(String[] args) {

        try {
            System.out.printf("%s + %s = ",args[0],args[1]);
            System.out.println( sum(args[0],args[1]) );
        } 
        catch(NumberFormatException iae) {
            System.err.println("êîílÇ≈ÇÕÇ†ÇËÇ‹ÇπÇÒÅI");
        }

    }

    static double sum(String a, String b) 
        throws NumberFormatException {
        
        return Double.parseDouble(a) + Double.parseDouble(b);
    }
}
