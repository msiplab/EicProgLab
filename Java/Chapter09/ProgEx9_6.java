public class ProgEx9_6 {

    public static void main(String args[]) {
	MyComplex z = new MyComplex();

	z.real = Double.parseDouble(args[0]);
	z.imag = Double.parseDouble(args[1]);

	display(z);

    }

    static void display(MyComplex z) {
	char s = ( z.imag < 0 ) ? '-' : '+';
	System.out.printf("%f %c i%f\n", z.real ,s, Math.abs(z.imag));
    }

}