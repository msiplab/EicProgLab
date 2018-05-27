public class MethodExample {

    public static void main(String args[]) {
	int a = Integer.parseInt(args[0]);
	int b = Integer.parseInt(args[1]);
	System.out.println("a+b= " + sum(a,b));
    }
    
    static int sum(int a, int b) {
	return a+b;
    }	
}
