import java.util.Scanner;

public class MatrixTranspositionStdIo {
    
    public static void main(String args[]) {
	
        /* 変数宣言 */
        Scanner scanner;
	double[][] matrix = new double[2][2];

	try {
	    
            /* 標準入力準備 */
	    scanner = new Scanner(System.in);
	    scanner.useDelimiter("\\s*,\\s*|\r\n");
	    
	    /* 標準入力 */
	    for (int iRow=0; iRow<2; iRow++)  {
		matrix[iRow][0] = scanner.nextDouble();
		matrix[iRow][1] = scanner.nextDouble();
	    }
	    
	    /* 標準出力 */
	    for (int iRow=0; iRow<2; iRow++) 
		System.out.printf("%f, %f\n", 
			      matrix[0][iRow], matrix[1][iRow]);

        } catch (Exception e) {
            System.err.println(e.getMessage());
	    System.exit(0);
        }
    }
}
