public class CatMain {
    
    public static void main(String args[]) {
	Cat tama = new Cat("タマ", "マグロ", 10);
	Cat mike = new Cat("ミケ", "サンマ", 5);
	
        System.out.println(tama.getName() +
			   "の体重: " +
			   tama.getWeight() + "kg");
        System.out.println(mike.getName() +
			   "の体重: " +
			   mike.getWeight() + "kg");
	tama.feed("マグロ");
	tama.feed("マグロ"); 
	tama.feed("マグロ");
	tama.feed("サンマ"); 
	mike.feed("マグロ");
	mike.feed("サンマ"); 
	
	System.out.println(tama.getName() +"の体重: " +
			   tama.getWeight() + "kg");
	System.out.println(mike.getName() +"の体重: " +
			   mike.getWeight() + "kg");
    }
}
