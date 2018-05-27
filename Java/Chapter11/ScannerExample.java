import java.util.Scanner;

public class ScannerExample {
    
    public static void main(String[] args) {
	
        Scanner scanner = new Scanner(System.in);
        double[][] matrix = new double[3][3];
	
        System.out.println("3x3行列の要素を入力して下さい:");
        for(int iRow = 0; iRow<3; iRow++) {
            for(int iCol = 0; iCol<3; iCol++) 
                matrix[iRow][iCol] = scanner.nextDouble();
        }

        System.out.println("\n3x3行列の要素は，");
        for(int iRow = 0; iRow<3; iRow++) {
            for(int iCol = 0; iCol<3; iCol++) 
                System.out.printf("%8.4g ", matrix[iRow][iCol]);
            System.out.println();
        }
    }

}
