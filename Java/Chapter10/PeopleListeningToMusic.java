public class PeopleListeningToMusic {
    
    public static void main(String args[]) {
	
	/* Person をインスタンス化 */
	Person taro = new Person("太郎", "アニメ");
	Person hanako = new Person("花子", "アイドル");

	/* Cd をインスタンス化 */
	Cd animeCd = new Cd("アニメ");

	/* CdPlayer をインスタンス化 */
	CdPlayer panasonyPlayer = new CdPlayer();
       
	/* panasonyPlayer に animeCd をセット */
	panasonyPlayer.setCd(animeCd);

	/* taro と hanako に Cd を聞かせる */
	taro.listenToMusic(panasonyPlayer);
	hanako.listenToMusic(panasonyPlayer);

	/* taro と hanako の気分は？ */
	System.out.println("太郎の気分： " + taro.kibun);
	System.out.println("花子の気分： " + hanako.kibun);
    }
}
