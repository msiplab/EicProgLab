import java.io.IOException; // ���o�͗�O�i��q�j

public class CharToCode {
    public static void main(String args[]) {
	
	try { // try-catch �ɂ��Ă͌�q
	    System.out.print("Input a character: ");
	    int c = System.in.read();
	    System.out.println("character '"+(char)c +
			       "' has a code number " + c + ".");
	} catch(IOException ioe) { // ��O����
	    System.err.println("IO Error");
	}
    }
}
