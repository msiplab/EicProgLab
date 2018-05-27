import java.io.File;
import java.io.PrintWriter;
import java.util.Scanner;
import java.io.FileNotFoundException;

public class MatrixTransposition {
    
    public static void main(String args[]) {
	
        /* �ϐ��錾 */
        File fin;
        File fout;
        Scanner scanner;
        PrintWriter writer;
	double[][] matrix = new double[2][2];

        /* �R�}���h�����̐��̊m�F */
        if ( args.length != 2 ) {
            System.out.println("\t�g�p�@: java " +
			       "MatrixTransposition " +
			       "[input file] [output file]");
            System.exit(0);
        }

	try {
	    
            /* ���̓t�@�C�� */
            fin = new File(args[0]);
	    scanner = new Scanner(fin);
	    scanner.useDelimiter("\\s*,\\s*|\r\n");
	    
	    /* �o�̓t�@�C�� */
	    fout = new File(args[1]);
            writer = new PrintWriter(fout);

	    /* �t�@�C������ */
	    for (int iRow=0; iRow<2; iRow++)  {
		matrix[iRow][0] = scanner.nextDouble();
		matrix[iRow][1] = scanner.nextDouble();
	    }
	    
	    /* �t�@�C���o�� */
	    for (int iRow=0; iRow<2; iRow++) 
		writer.printf("%f, %f\n", 
			      matrix[0][iRow], matrix[1][iRow]);

            /* �t�@�C���̃N���[�Y */
            scanner.close();
            writer.close();
	    
        } catch (FileNotFoundException fnfe)  {
            System.err.println(fnfe.getMessage());
	    System.exit(0);
        }
    }
}
