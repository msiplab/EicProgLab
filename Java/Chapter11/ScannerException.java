import java.util.Scanner;
import java.util.InputMismatchException;

public class ScannerException {
    
    public static void main(String[] args) {
	
	Scanner scanner = new Scanner(System.in);
	double[][] matrix = new double[3][3];
	
	try {
	    System.out.println("3x3s—ñ‚Ì—v‘f‚ğ“ü—Í‚µ‚Ä‰º‚³‚¢:");
	    for(int iRow = 0; iRow<3; iRow++) {
		for(int iCol = 0; iCol<3; iCol++) 
		    matrix[iRow][iCol] = scanner.nextDouble();
	    }
	} catch (InputMismatchException ime) {
	    System.err.println("doubleŒ^‚Ì”’l‚ğ“ü—Í‚µ‚Ä‰º‚³‚¢.");
	    System.exit(0);
	}
    }
}
