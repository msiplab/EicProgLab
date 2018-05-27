public class ProgEx9_2 {
	public static void main(String args[]) {

		double[][] a = { {1.0},
				{1.0, 2.0},
				{1.0, 2.0, 3.0} };
		
		for(int i=0; i<a.length; i++) {
			for(int j=0; j<a[i].length; j++)
				System.out.print(a[i][j]+" ");
			System.out.println();
		}
	}
}
