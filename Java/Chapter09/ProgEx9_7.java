public class ProgEx9_7 {

    public static void main(String args[]) {
	MyComplex z1 = new MyComplex();
	MyComplex z2 = new MyComplex();

	z1.real = Double.parseDouble(args[0]);
	z1.imag = Double.parseDouble(args[1]);
	
	z2.real = Double.parseDouble(args[2]);
	z2.imag = Double.parseDouble(args[3]);

	z1.display();
	z2.display();
    }
}
