public class PeopleApplication {
    
    public static void main(String args[]) {
	
	Person taro = new Person("太郎", "アニメ");
	Person hanako = new Person("花子", "アイドル");
	
	System.out.println("太郎の気分： " + taro.kibun);
	System.out.println("花子の気分： " + hanako.kibun);
	
    }
}
