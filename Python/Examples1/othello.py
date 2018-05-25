class PointState:
    def __init__(self, mark):
        self.__mark = mark
    def __str__(self):
        return self.__mark 

class BoardOutOfRangeException(Exception):
    def __init__(self, e):
        Exception.__init__(self, e)

class Board:

    __NONE = PointState('.')
    __BLACK_STONE = PointState('B')
    __WHITE_STONE = PointState('W')

    def __init__(self):
        self.__currentStone = Board.__BLACK_STONE
        self.__stateArray = [ [ Board.__NONE
                                for irow in range(1,9) ]
                                for icol in range(1,9) ]
        self.__setState(4, 4, Board.__WHITE_STONE)
        self.__setState(5, 4, Board.__BLACK_STONE)
        self.__setState(4, 5, Board.__BLACK_STONE)
        self.__setState(5, 5, Board.__WHITE_STONE)

    def displayState(self):
        try:
            print('\n 12345678')
            for y in range(1,9):
                print(y, end='')
                for x in range(1,9):
                    state = self._getState(x, y)
                    print(state,end='')
                print()
            print('現在の手番：',end='')
            if self.__currentStone == Board.__BLACK_STONE:
                print('黒(B)')
            else:
                print('白(W)')            
        except BoardOutOfRangeException as boore:
            print(boore.message)

    def change(self):
        self.__currentStone = self.__getEnemyStone()

    def tryPlaceStone(self, x, y):
        if self._getState(x,y) != Board.__NONE:
            return False
        trial = False
        trial = trial | self.__tryReverseNext(x, y, +1,  0) # 右
        trial = trial | self.__tryReverseNext(x, y,  0, +1) # 下
        trial = trial | self.__tryReverseNext(x, y, -1,  0) # 左
        trial = trial | self.__tryReverseNext(x, y,  0, -1) # 上
        trial = trial | self.__tryReverseNext(x, y, +1, +1) # 右下
        trial = trial | self.__tryReverseNext(x, y, +1, -1) # 右上
        trial = trial | self.__tryReverseNext(x, y, -1, +1) # 左下
        trial = trial | self.__tryReverseNext(x, y, -1, -1) # 上上
        if trial: # 隣の石を返すことができる場合
            # 石を置いてボードの状態を更新する。
            self.__setState(x, y, self.__currentStone)
            # 手番を相手に渡す
            self.change()
            
    def _getState(self, x, y):
        if x < 1 or x > 8 or y < 1 or y > 8:
            raise BoardOutOfRangeException('xとyは、0以上かつ9以下の値でなければなりません。')
        return self.__stateArray[x-1][y-1]
    
    def __tryReverseNext(self, x, y, dx, dy):
        try:
            if self._getState(x+dx, y+dy) == self.__getEnemyStone():
                if self._getState(x+dx+dx,y+dy+dy) == self.__currentStone:
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
            return False
    
    def __setState(self, x, y, state):
        self.__stateArray[x-1][y-1] = state

    def __getEnemyStone(self):
        if self.__currentStone == Board.__BLACK_STONE:
            return Board.__WHITE_STONE
        else:
            return Board.__BLACK_STONE
