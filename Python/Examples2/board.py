from point_state import PointState
from board_out_of_range_exception import BoardOutOfRangeException

class Board:
    """リバーシ（オセロ）の盤クラス"""
    
    # このクラスと派生クラスでしか使わない定数
    _NONE = PointState('.')
    _BLACK_STONE = PointState('B')
    _WHITE_STONE = PointState('W')

    def __init__(self):
        """コンストラクタ"""        
        # 最初の手番を黒に設定
        self.__currentStone = Board._BLACK_STONE        
        # 盤上の石をすべてクリア(_NONE)と設定
        self.__stateArray = [ [ Board._NONE
                                for irow in range(1,9) ]
                                for icol in range(1,9) ]        
        # 盤を初期状態にするために石を置く
        self.__setState(4, 4, Board._WHITE_STONE)
        self.__setState(5, 4, Board._BLACK_STONE)
        self.__setState(4, 5, Board._BLACK_STONE)
        self.__setState(5, 5, Board._WHITE_STONE)
        

    def displayState(self):
        """盤の状態表示"""
        try:
            # 列番号の表示
            print('\n 12345678') 
            for y in range(1,9):
                # 行番号の表示
                print(y, end='')
                for x in range(1,9):
                    # x列目，y行目のマスの状態
                    state = self._getState(x, y)
                    print(state,end='')
                print()
            print()
            # 現在の手番の色の表示
            print('現在の手番：',end='')
            if self.__currentStone == Board._BLACK_STONE:
                print('黒(B)')
            else:
                print('白(W)')            
        except BoardOutOfRangeException as boore:
            print(boore.message)

    def change(self):
        """パス"""
        self.__currentStone = self.__getEnemyStone()

    def tryPlaceStone(self, x, y):
        """
        座標(x,y)に石を試しに置く。
        石を置こうとする場所が盤の範囲外であれば例外を投げる。
        """
        # 例外を萎える可能性あり
        if self._getState(x,y) != Board._NONE:
            return False
        # 石を置こうとする場所の隣を返せるかどうかを確認
        trial = False
        trial = trial | self.__tryReverseNext(x, y, +1,  0) # 右
        trial = trial | self.__tryReverseNext(x, y,  0, +1) # 下
        trial = trial | self.__tryReverseNext(x, y, -1,  0) # 左
        trial = trial | self.__tryReverseNext(x, y,  0, -1) # 上
        trial = trial | self.__tryReverseNext(x, y, +1, +1) # 右下
        trial = trial | self.__tryReverseNext(x, y, +1, -1) # 右上
        trial = trial | self.__tryReverseNext(x, y, -1, +1) # 左下
        trial = trial | self.__tryReverseNext(x, y, -1, -1) # 左上
        # 隣の石を返すことができる場合
        if trial: 
            # 石を置いてボードの状態を更新する
            self.__setState(x, y, self.__currentStone)
            # 手番を相手に渡す
            self.change()
            
    def _getState(self, x, y):
        """指定した位置のマスの状態を取得"""
        
        # マスの範囲外であれば例外を投げる
        if x < 1 or x > 8 or y < 1 or y > 8:
            raise BoardOutOfRangeException(
                       'xとyは、0以上かつ9以下の値でなければなりません。')
        # 盤のx列目，y行目の状態をリターン
        return self.__stateArray[x-1][y-1]
    
    def __tryReverseNext(self, x, y, dx, dy):
        try:
            # 隣の石が相手の石であるかどうかの確認
            if self._getState(x+dx, y+dy) == self.__getEnemyStone():
                # 隣の隣の石が自分の石であるかどうかの確認
                if self._getState(x+dx+dx,y+dy+dy) == self.__currentStone:
                    # 隣の石が相手で，隣の隣の石が自分である場合，石を返して盤を更新
                    self.__setState(x+dx, y+dy, self.__currentStone)
                    return True
                elif self.__tryReverseNext(x+dx, y+dy, dx, dy):
                    self.__setState(x+dx, y+dy, self.__currentStone)
                    return True
                else:
                    return False
            else:
                return False
        except BoardOutOfRangeException as boore:
            # 盤の範囲外にアクセスがあれば失敗
            return False
    
    def __setState(self, x, y, state):
        """盤のx列目y行目のマスの状態を与えられた状態に更新"""
        self.__stateArray[x-1][y-1] = state

    def __getEnemyStone(self):
        """相手（次の手番）の色を取得"""
        if self.__currentStone == Board._BLACK_STONE:
            return Board._WHITE_STONE
        else:
            return Board._BLACK_STONE
