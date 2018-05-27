public class ProgEx9_4 {

	static int nCalls; 

	public static void main(String args[]) {
		nCalls = 0;
		for (int i=0; i<10; i++)
			System.out.println(count());
	}

	static int count() {
		return nCalls++;
	}	
}
