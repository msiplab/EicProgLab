public class StringMethods {
    public static void main(String args[]) {
	
	String strJava1 = "Java"; // new String("Java") ‚Æ“¯‚¶
	System.out.println("strJava1 = " + strJava1);
	
        char charArray[] = { 'J', 'a', 'v', 'a' };
        String strJava2 = new String(charArray);
        System.out.println("strJava2 = " + strJava2);
	
        System.out.println("strJava2.replace('a','o') = " + 
			   strJava2.replace('a','o'));
	
        System.out.println("strJava2.toLowerCase() = " + 
			   strJava2.toLowerCase());
    }
}
