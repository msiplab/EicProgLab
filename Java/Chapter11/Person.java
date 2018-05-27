public class Person {
    private String _name;
    private String _konomi;
    private String _kibun = "普通";
    
    public Person(String name, String konomi) {
        _name = name;
        _konomi = konomi;
    }
    
    public void listenToMusic(CdPlayer cdPlayer) {
	String genre = cdPlayer.playCd();
        if (genre.equals(_konomi))
	    _kibun = "楽しい";
        else 
	    _kibun = "イライラ";
    }

    public String getKibun() {
	return _kibun;
    }
    
    public String getName() {
        return _name;
    }

}
