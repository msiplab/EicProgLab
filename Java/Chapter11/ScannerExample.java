import java.util.Scanner;

public class ScannerExample {
    
    public static void main(String[] args) {
	
        Scanner scanner = new Scanner(System.in);
        double[][] matrix = new double[3][3];
	
        System.out.println("3x3�s��̗v�f����͂��ĉ�����:");
        for(int iRow = 0; iRow<3; iRow++) {
            for(int iCol = 0; iCol<3; iCol++) 
                matrix[iRow][iCol] = scanner.nextDouble();
        }

        System.out.println("\n3x3�s��̗v�f�́C");
        for(int iRow = 0; iRow<3; iRow++) {
            for(int iCol = 0; iCol<3; iCol++) 
                System.out.printf("%8.4g ", matrix[iRow][iCol]);
            System.out.println();
        }
    }

}
