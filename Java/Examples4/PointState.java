public class PointState {

    private char _mark;
    
    /* コンストラクタ （外部からの利用を不可とする）*/
    private PointState() {}
    
    /* コンストラクタ */
    public PointState(char mark){
	_mark = mark;
    }
    
    /* 文字列への変換 */
    public String toString() {
	return new Character(_mark).toString();
    }
}
