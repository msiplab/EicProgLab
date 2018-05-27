import java.io.IOException; // 入出力例外（後述）

public class CharToCode {
    public static void main(String args[]) {
	
	try { // try-catch については後述
	    System.out.print("Input a character: ");
	    int c = System.in.read();
	    System.out.println("character '"+(char)c +
			       "' has a code number " + c + ".");
	} catch(IOException ioe) { // 例外処理
	    System.err.println("IO Error");
	}
    }
}
