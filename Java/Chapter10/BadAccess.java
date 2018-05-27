public class BadAccess {
    
    public static void displayTop(MyStack myStack) {
	System.out.println("Top: " + myStack.top);
	myStack.top = 0;
    }

}
