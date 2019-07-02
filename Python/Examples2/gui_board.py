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
    
    
    def display_state(self):
        """ボードの状態の表示"""
        try:
            # ボード状態の更新
            for y in range(1,9):
                for x in range(1,9):
                    if self._get_state(x, y) == Board._WHITE_STONE:
                        self.__table.set_cell_foreground(x,y,'white')
                    elif self._get_state(x, y) == Board._BLACK_STONE:
                        self.__table.set_cell_foreground(x,y,'black')
        except BoardOutOfRangeException as boore:
            # 例外処理
            print()
            print(boore)            
        finally:
            # 表示の更新
            self.__root.update()
            super().display_state()
            time.sleep(1)


class BoardTable(Frame):
    """ボード用のテーブル"""
    
    def __init__(self,master=None):
        """コンストラクタ"""
        super().__init__(master)
        self['padding']=(20,20)
        self.pack()
        self.create_style()
        self.create_widgets()
        
        
    def create_style(self):
        """スタイルの生成"""
        # ラベルのスタイル
        style = Style()
        style.configure('C.TLabel',
            borderwidth = 2,
            padding = (6,0),
            relief = RIDGE,
            font = ('Helvetica', '16'),
            background='green',
            foreground='green')
    
    
    def create_widgets(self):
        """ウィジットの生成"""
        # マス目ラベルの生成
        self.__cells = [ [ Label(self, text='●', style='C.TLabel')
                            for icol in range(8) ] 
                            for irow in range(8) ]
        # マス目ラベルのグリッド配置
        for irow  in range(8):
            for icol in range(8):
                cell = self.__cells[irow][icol]
                cell.grid(row=irow, column=icol)
                                                
    def set_cell_foreground(self, x, y, fgcolor):
        """コマの色の更新"""
        self.__cells[y-1][x-1]['foreground'] = fgcolor

 
if __name__ == '__main__':
    board = GuiBoard()
