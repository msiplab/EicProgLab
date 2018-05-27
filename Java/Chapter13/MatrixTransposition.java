import java.io.File;
import java.io.PrintWriter;
import java.util.Scanner;
import java.io.FileNotFoundException;

public class MatrixTransposition {
    
    public static void main(String args[]) {
	
        /* 変数宣言 */
        File fin;
        File fout;
        Scanner scanner;
        PrintWriter writer;
	double[][] matrix = new double[2][2];

        /* コマンド引数の数の確認 */
        if ( args.length != 2 ) {
            System.out.println("\t使用法: java " +
			       "MatrixTransposition " +
			       "[input file] [output file]");
            System.exit(0);
        }

	try {
	    
            /* 入力ファイル */
            fin = new File(args[0]);
	    scanner = new Scanner(fin);
	    scanner.useDelimiter("\\s*,\\s*|\r\n");
	    
	    /* 出力ファイル */
	    fout = new File(args[1]);
            writer = new PrintWriter(fout);

	    /* ファイル入力 */
	    for (int iRow=0; iRow<2; iRow++)  {
		matrix[iRow][0] = scanner.nextDouble();
		matrix[iRow][1] = scanner.nextDouble();
	    }
	    
	    /* ファイル出力 */
	    for (int iRow=0; iRow<2; iRow++) 
		writer.printf("%f, %f\n", 
			      matrix[0][iRow], matrix[1][iRow]);

            /* ファイルのクローズ */
            scanner.close();
            writer.close();
	    
        } catch (FileNotFoundException fnfe)  {
            System.err.println(fnfe.getMessage());
	    System.exit(0);
        }
    }
}
