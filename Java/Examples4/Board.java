public class Board {
    
    /* このクラスでしか使わない定数 */
    private static final PointState _NONE = new PointState('.');
    private static final PointState _BLACK_STONE = new PointState('B');
    private static final PointState _WHITE_STONE = new PointState('W');
    
    /* このクラスでしか使わない変数 */
    private PointState[][] _stateArray = new PointState[8][8];
    private PointState _currentStone; 

    /* コンストラクタ */
    public Board() {
	
    	/* 最初の手番を黒に設定 */
    	_currentStone = _BLACK_STONE;
	
    	/* 盤上の石を全てクリア(_NONEと設定) */
    	for(int x=1; x<9; x++) 
	    for(int y=1; y<9; y++) 
		_setState(x, y, _NONE);
	
    	/* 盤を初期状態にするために石を置く */
    	_setState(4, 4, _WHITE_STONE);
    	_setState(5, 4, _BLACK_STONE);
    	_setState(4, 5, _BLACK_STONE);
    	_setState(5, 5, _WHITE_STONE);
	
    }
    
    /* ボードの状態の表示 */
    public void displayState() {
    	try {
	    System.out.println("\n 12345678"); /* 列番号の表示 */
	    for (int y = 1; y < 9; y++) {
		System.out.print(y); /* 行番号の表示 */
		for (int x = 1; x < 9; x++) {
		    /* x列目、y行目のマスの状態 */
		    PointState state = _getState(x, y);
		    System.out.print(state);
		}
		System.out.println();
	    }
	    System.out.println();
	    /* 現在の手番の色の表示 */
	    System.out.println("現在の手番: " +  
			       (_currentStone == _BLACK_STONE ?
				"黒(B)" : "白(W)") );
    	} catch (BoardOutOfRangeException boore) {
	    System.out.println(boore.getMessage());
    	}
    }  
    
    /* パス */
    public void pass() {
    	_currentStone = _getEnemyStone();
    }
    
    /*
     * 座標(x,y)に石を試しに置く。
     * 石を置こうとする場所がボードの範囲外であれば例外を投げる
     */
    public boolean tryPlaceStone(int x, int y) 
    	throws BoardOutOfRangeException {
	
    	/* 石を置こうとする場所に既に石があれば失敗 */
    	if ( _getState(x, y) != _NONE ) // 例外をスローする可能性あり
	    return false;
	
    	/* 石を置こうとする場所の隣を返せるかどうかを確認 */
    	boolean trial = false;
    	trial = trial | _tryReverseNext(x, y, +1,  0); /* 右 */
    	trial = trial | _tryReverseNext(x, y,  0, +1); /* 下 */
    	trial = trial | _tryReverseNext(x, y, -1,  0); /* 左 */
    	trial = trial | _tryReverseNext(x, y,  0, -1); /* 上 */
    	trial = trial | _tryReverseNext(x, y, +1, +1); /* 右下 */
    	trial = trial | _tryReverseNext(x, y, +1, -1); /* 右上 */
    	trial = trial | _tryReverseNext(x, y, -1, +1); /* 左下 */
    	trial = trial | _tryReverseNext(x, y, -1, -1); /* 上上 */
    	if (trial) { /* 隣の石を返すことができる場合*/
	    /* 石を置いてボードの状態を更新する。*/
	    _setState(x, y, _currentStone);
	    /* 手番を相手に渡す */
	    _currentStone = _getEnemyStone();
    	}	
    	return trial;
    }
    
    /* 指定した位置のボードの状態を取得 */
    protected PointState _getState(int x, int y) 
	throws BoardOutOfRangeException { // 例外をスロー
	
    	if (x < 1 || x > 8 
	    || y < 1 || y > 8) { // マスの範囲外であれば例外をスロー
	    throw new BoardOutOfRangeException(
		  "xとyは、0 以上かつ9以下の値でなければなりません。");
    	}
    	/* 盤のx列目、y行目の状態をリターン */
    	return _stateArray[x-1][y-1]; 
    }
    
    private boolean _tryReverseNext(int x, int y, int dx, int dy) {
    	try {
	    /* 隣の石が相手の石であるかどうかの確認 */
	    if(_getState(x + dx, y + dy) == _getEnemyStone()) {
		/* 隣の隣の石が自分の石であるかどうかの確認 */
		if (_getState(x+dx+dx, y+dy+dy) == _currentStone ) {
		    /* 隣の石が相手で、隣の隣の石が自分である場合、
		       石を返して盤を更新 */
		    _setState(x+dx, y+dy, _currentStone);
		    return true;
		} else if (_tryReverseNext(x + dx, y + dy, dx, dy )){
		    _setState(x+dx, y+dy, _currentStone);
		    return true;
		} else 
		    return false;
	    } else
		return false;
    	} catch (BoardOutOfRangeException boore) {
	    /* ボードの範囲外にアクセスがあれば失敗 */
	    return false;
    	}
    }
    
    private void _setState(int x, int y, PointState state) {
    	/* 盤のx列目y行目のマスの状態を与えられた状態に更新 */
    	_stateArray[x-1][y-1] = state;
    }
    
    private PointState _getEnemyStone() {
    	/* 相手（次の手番）の色の取得 */
    	return _currentStone == _BLACK_STONE ? 
	    _WHITE_STONE : _BLACK_STONE;
    }

}
