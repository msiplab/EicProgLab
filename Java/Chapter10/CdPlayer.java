public class CdPlayer {
    private Cd _cd;
    
    public CdPlayer() {}
    
    public void setCd(Cd cd) {
        _cd = cd;
    }
    
    public String playCd() {
        return _cd.getGenre();
    }
}
