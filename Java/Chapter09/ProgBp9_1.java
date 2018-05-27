public class ProgBp9_1 {

	public static void main(String args[]) {
		double angle;
		double real = Math.sqrt(3)/2.0;
		double imag = 0.5;

		angle = Math.atan2(imag, real)*180.0/Math.PI;

		System.out.println(angle);
	}
}
