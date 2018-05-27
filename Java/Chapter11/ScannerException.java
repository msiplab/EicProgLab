import java.util.Scanner;
import java.util.InputMismatchException;

public class ScannerException {
    
    public static void main(String[] args) {
	
	Scanner scanner = new Scanner(System.in);
	double[][] matrix = new double[3][3];
	
	try {
	    System.out.println("3x3�s��̗v�f����͂��ĉ�����:");
	    for(int iRow = 0; iRow<3; iRow++) {
		for(int iCol = 0; iCol<3; iCol++) 
		    matrix[iRow][iCol] = scanner.nextDouble();
	    }
	} catch (InputMismatchException ime) {
	    System.err.println("double�^�̐��l����͂��ĉ�����.");
	    System.exit(0);
	}
    }
}
