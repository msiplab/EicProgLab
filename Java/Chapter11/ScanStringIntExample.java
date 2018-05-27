import java.util.Scanner;
public class ScanStringIntExample {
    
    public static void main(String[] args) {
	
	Scanner scanner = new Scanner(System.in);
	String name;
	int age;
	
	System.out.println("名前を入力して下さい");
	
	name = scanner.next();

	System.out.println("年齢を入力して下さい");
	
	age = scanner.nextInt();

	System.out.printf("名前：%s （%d歳）\n",name,age);

    }
}
