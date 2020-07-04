from tkinter import *
from tkinter.ttk import *
from board import Board
from board_out_of_range_exception import BoardOutOfRangeException
import time

class GuiBoard(Board):

    def __init__(self,master=None,verbose=False):
        """コンストラクタ"""        
        # Board クラスのコンストラクタを呼び出し
        super().__init__(verbose) 
        if master == None:
            self.__root = Tk()
        else:
            self.__root = master
        self.__root.title('リバーシ')
        self.__table = BoardTable(self.__root)
        self.display_state()
    
    def display_state(self):
        """ボードの状態の表示"""
        try:
            # ボード状態の更新
            for y in range(1,9):
                for x in range(1,9):
                    if self._get_cell_state(x, y) == Board.WHITE:
                        self.__table.set_cell_stone(x,y,Board.WHITE)
                    elif self._get_cell_state(x, y) == Board.BLACK:
                        self.__table.set_cell_stone(x,y,Board.BLACK)
                    else:
                        self.__table.set_cell_stone(x,y,Board.EMPTY)
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

    def __init__(self,master=None,ndims=[8,8]):
        """コンストラクタ"""
        super().__init__(master)
        self.ndims = ndims
        self['padding']=(20,20)
        self.pack()
        self.create_style()
        self.create_images()                
        self.create_widgets()
        
    def create_style(self):
        """スタイルの生成"""
        # ラベルのスタイル
        style = Style()
        style.configure('My.TButton',
            borderwidth = 0,
            padding = (0,0),
            relief = RIDGE,
            background='green')
        # ラベルのスタイル            
        style.configure('My.TLabel',
            font = ('Helvetica', '12'),
            anchor = 'center',
            background='green',
            foreground='white')            

    def create_images(self):
        """マス目の画像生成"""
        self.empty_img = PhotoImage(file = r"empty.png").subsample(2,2)        
        self.white_img = PhotoImage(file = r"white.png").subsample(2,2)        
        self.black_img = PhotoImage(file = r"black.png").subsample(2,2)                                

    def create_widgets(self):
        """ウィジットの生成"""
        # 配列の行数(nrows)と列数(ncols)        
        nrows = self.ndims[0]
        ncols = self.ndims[1]
        # マス目ラベルの生成
        self.__cells = [ [ Button(self, image=self.empty_img, style='My.TButton')
                            for icol in range(ncols) ] 
                            for irow in range(nrows) ]
        # マス目ラベルのグリッド配置
        for irow in range(nrows):
            for icol in range(ncols):
                cell = self.__cells[irow][icol]
                cell.grid(row=irow, column=icol)
                cell.image = self.empty_img
                # 左クリック時の動作の登録
                cell.bind('<Button-1>', self.press)                
        # ラベルの生成
        self.__var = StringVar()
        label = Label(self, style='My.TLabel')
        label.config(textvariable = self.__var)
        self.__var.set('(-,-)')
        label.grid(row=nrows+1, column=0, columnspan=ncols, sticky=(W,E))                

    def press(self,event):
        """ボタンクリックの動作"""
        irow = event.widget.grid_info()['row']
        icol = event.widget.grid_info()['column']        
        self.__var.set('({0},{1})'.format(irow,icol))

    def set_cell_stone(self, x, y, stone):
        """コマの色の更新"""
        if stone == Board.WHITE:
            self.__cells[y-1][x-1]['image'] = self.white_img
        elif stone == Board.BLACK:
            self.__cells[y-1][x-1]['image'] = self.black_img
        else:
            self.__cells[y-1][x-1]['image'] = self.empty_img

if __name__ == '__main__':
    root = Tk()
    board = GuiBoard(root)
    root.mainloop()
