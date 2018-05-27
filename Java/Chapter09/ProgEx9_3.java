public class ProgEx9_3 {
    public static void main(String args[]) {
	
	double[] x = { 1.0, 3.0 };     // vector x
	double[][] A = { {  .5, .5 },  // matrix A 
		       { -.5, .5 } };
	double[] y = new double[2];    // vector y

	for(int i=0; i<y.length; i++) { // y = Ax
	    y[i] = 0.0;                  
	    for(int j=0; j<x.length; j++)
		y[i] += A[i][j] * x[j]; 
	}

	for(int i=0; i<y.length; i++)
	    System.out.println(y[i]);   // display y
    }
}
