public class Person {

    private String _name;
    private String _konomi;
    public String kibun = "•’Ê";
    
    public Person(String name, String konomi) {
        this._name = name;
        this._konomi = konomi;
    }
    
    public void listenToMusic(CdPlayer cdPlayer) {
	String genre = cdPlayer.playCd();
        if (genre.equals(this._konomi))
	    this.kibun = "Šy‚µ‚¢";
        else 
	    this.kibun = "ƒCƒ‰ƒCƒ‰";
    }

}
