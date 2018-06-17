from tkinter import *
from tkinter.ttk import *
from board import Board
from board_out_of_range_exception import BoardOutOfRangeException
import time

class GuiBoard(Board):  
    
    def __init__(self):
        """コンストラクタ"""        
        # Board クラスのコンストラクタを呼び出し
        super().__init__()         
        self.__root = Tk()
        self.__root.title('オセロ')         
        self.__table = BoardTable(self.__root)
    
    
    def displayState(self):
        """ボードの状態の表示"""
        try:
            for y in range(1,9):
                for x in range(1,9):
                    if self._getState(x, y) == Board._WHITE_STONE:
                        self.__table.setCellFg(x,y,'white')
                    elif self._getState(x, y) == Board._BLACK_STONE:
                        self.__table.setCellFg(x,y,'black')
        except BoardOutOfRangeException as boore:
            print()
            print(boore)            
        finally:
            self.__root.update()
            super().displayState()
            time.sleep(1)


class BoardTable(Frame):
    """ボード用のテーブル"""
    
    def __init__(self,master=None):        
        super().__init__(master)
        self['padding']=(20,20)
        self.pack()
        self.create_widgets()
        
        
    def create_widgets(self):
        self.__cells = [ [ BoardCell(self) 
                            for icol in range(8) ] 
                            for irow in range(8) ]
        for irow  in range(8):
            for icol in range(8):
                self.__cells[irow][icol].grid(row=irow, 
                                                 column=icol)
                                                
    def setCellFg(self, x, y, fgcolor):
        self.__cells[y-1][x-1]['foreground'] = fgcolor
        

class BoardCell(Label):
    """マス目の設定"""
    def __init__(self,master=None):
        super().__init__(master)
        self['borderwidth'] = 2
        self['padding'] = (6,0)
        self['relief'] = RIDGE
        self['font'] = ('Helvetica','16')   
        self['text'] = '●'
        self['background']='green'
        self['foreground']='green'

 
if __name__ == '__main__':
    
    board = GuiBoard()
    
