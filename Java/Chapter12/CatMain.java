public class CatMain {
    
    public static void main(String args[]) {
	Cat tama = new Cat("�^�}", "�}�O��", 10);
	Cat mike = new Cat("�~�P", "�T���}", 5);
	
        System.out.println(tama.getName() +
			   "�̑̏d: " +
			   tama.getWeight() + "kg");
        System.out.println(mike.getName() +
			   "�̑̏d: " +
			   mike.getWeight() + "kg");
	tama.feed("�}�O��");
	tama.feed("�}�O��"); 
	tama.feed("�}�O��");
	tama.feed("�T���}"); 
	mike.feed("�}�O��");
	mike.feed("�T���}"); 
	
	System.out.println(tama.getName() +"�̑̏d: " +
			   tama.getWeight() + "kg");
	System.out.println(mike.getName() +"�̑̏d: " +
			   mike.getWeight() + "kg");
    }
}
