import java.util.Scanner;
public class ScanStringIntExample {
    
    public static void main(String[] args) {
	
	Scanner scanner = new Scanner(System.in);
	String name;
	int age;
	
	System.out.println("���O����͂��ĉ�����");
	
	name = scanner.next();

	System.out.println("�N�����͂��ĉ�����");
	
	age = scanner.nextInt();

	System.out.printf("���O�F%s �i%d�΁j\n",name,age);

    }
}
