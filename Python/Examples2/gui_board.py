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
            self.master = Tk()
            self.master.title('リバーシ')
        else:
            self.master = master
        self.__table = BoardTable(master) # self)
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
            self.master.update()
            super().display_state()
            time.sleep(1)

class BoardTable(Frame):
    """ボード用のテーブル"""

    NUM_DIMS = [8,8]

    def __init__(self,master): # ,board):
        """コンストラクタ"""
        super().__init__(master) # board.master)
        #self.__board = board
        self['padding']=(20,20)
        self.pack()
        self.create_style()
        self.create_images()                
        self.create_widgets()
        
    def create_style(self):
        """スタイルの生成"""
        # ボタンのスタイル
        style = Style()
        style.configure('MyCell.TButton',
            borderwidth = 0,
            padding = (0,0),
            relief = RIDGE,
            background='green')
        # ラベルのスタイル            
        #style.configure('MyInfo.TLabel',
            #font = ('Helvetica', '12'),
            #anchor = 'center',
            #background='green',
            #foreground='white') 

    def create_images(self):
        """マス目の画像生成"""
        self.empty_img = PhotoImage(file = r"empty.png").subsample(2,2)        
        self.white_img = PhotoImage(file = r"white.png").subsample(2,2)        
        self.black_img = PhotoImage(file = r"black.png").subsample(2,2)                                

    def create_widgets(self):
        """ウィジットの生成"""
        # 配列の行数(nrows)と列数(ncols)        
        nrows = BoardTable.NUM_DIMS[0]
        ncols = BoardTable.NUM_DIMS[1]
        # マス目ラベルの生成
        self.__cells = [ [ Button(self, image=self.empty_img, style='MyCell.TButton')
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
        # 情報ラベルの生成
        #self.__var = StringVar()
        #label = Label(self, style='MyInfo.TLabel')
        #label.config(textvariable = self.__var)
        #self.__var.set('(-,-)')
        #label.grid(row=nrows+1, column=0, columnspan=ncols, sticky=(W,E))                

    def press(self,event):
        """ボタンクリックの動作"""
        x = event.widget.grid_info()['column'] + 1              
        y = event.widget.grid_info()['row'] + 1
        print('({0},{1})'.format(x,y))
        #self.__board.try_place_stone(x, y)
        #self.__board.display_state()
        #self.__var.set('({0},{1})'.format(x,y))

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
    root.title('リバーシ')    
    board = GuiBoard(root,verbose=True)
    root.mainloop()
