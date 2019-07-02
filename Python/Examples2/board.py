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
        self.__current_stone = Board._BLACK_STONE        
        # 盤上の石をすべてクリア(_NONE)と設定
        self.__state_array = [ [ Board._NONE
                                for irow in range(1,9) ]
                                for icol in range(1,9) ]        
        # 盤を初期状態にするために石を置く
        self.__set_state(4, 4, Board._WHITE_STONE)
        self.__set_state(5, 4, Board._BLACK_STONE)
        self.__set_state(4, 5, Board._BLACK_STONE)
        self.__set_state(5, 5, Board._WHITE_STONE)
        

    def display_state(self):
        """盤の状態表示"""
        try:
            # 列番号の表示
            print('\n 12345678') 
            for y in range(1,9):
                # 行番号の表示
                print(y, end='')
                for x in range(1,9):
                    # x列目，y行目のマスの状態
                    state = self._get_state(x, y)
                    print(state,end='')
                print()
            print()
            # 現在の手番の色の表示
            print('現在の手番：',end='')
            if self.__current_stone == Board._BLACK_STONE:
                print('黒(B)')
            else:
                print('白(W)')            
        except BoardOutOfRangeException as boore:
            print(boore.message)

    def change(self):
        """パス"""
        self.__current_stone = self.__get_enemy_stone()

    def try_place_stone(self, x, y):
        """
        座標(x,y)に石を試しに置く。
        石を置こうとする場所が盤の範囲外であれば例外を投げる。
        """
        # 例外を投げる可能性あり
        if self._get_state(x,y) != Board._NONE:
            return False
        # 石を置こうとする場所の隣を返せるかどうかを確認
        trial = False
        trial = trial | self.__try_reverse_next(x, y, +1,  0) # 右
        trial = trial | self.__try_reverse_next(x, y,  0, +1) # 下
        trial = trial | self.__try_reverse_next(x, y, -1,  0) # 左
        trial = trial | self.__try_reverse_next(x, y,  0, -1) # 上
        trial = trial | self.__try_reverse_next(x, y, +1, +1) # 右下
        trial = trial | self.__try_reverse_next(x, y, +1, -1) # 右上
        trial = trial | self.__try_reverse_next(x, y, -1, +1) # 左下
        trial = trial | self.__try_reverse_next(x, y, -1, -1) # 左上
        # 隣の石を返すことができる場合
        if trial: 
            # 石を置いてボードの状態を更新する
            self.__set_state(x, y, self.__current_stone)
            # 手番を相手に渡す
            self.change()
        # 石を置けたら True, 置けなければ False を返す
        return trial
    
    def _get_state(self, x, y):
        """指定した位置のマスの状態を取得"""
        
        # マスの範囲外であれば例外を投げる
        if x < 1 or x > 8 or y < 1 or y > 8:
            raise BoardOutOfRangeException(
                       'xとyは、1以上かつ8未満の値でなければなりません。')
        # 盤のx列目，y行目の状態をリターン
        return self.__state_array[x-1][y-1]
    
    def __try_reverse_next(self, x, y, dx, dy):
        try:
            # 隣の石が相手の石であるかどうかの確認
            if self._get_state(x+dx, y+dy) == self.__get_enemy_stone():
                # 隣の隣の石が自分の石であるかどうかの確認
                if self._get_state(x+dx+dx,y+dy+dy) == self.__current_stone:
                    # 隣の石が相手で，隣の隣の石が自分である場合，石を返して盤を更新
                    self.__set_state(x+dx, y+dy, self.__current_stone)
                    return True
                elif self.__try_reverse_next(x+dx, y+dy, dx, dy):
                    self.__set_state(x+dx, y+dy, self.__current_stone)
                    return True
                else:
                    return False
            else:
                return False
        except BoardOutOfRangeException as boore:
            # 盤の範囲外にアクセスがあれば失敗
            return False
    
    def __set_state(self, x, y, state):
        """盤のx列目y行目のマスの状態を与えられた状態に更新"""
        self.__state_array[x-1][y-1] = state

    def __get_enemy_stone(self):
        """相手（次の手番）の色を取得"""
        if self.__current_stone == Board._BLACK_STONE:
            return Board._WHITE_STONE
        else:
            return Board._BLACK_STONE
