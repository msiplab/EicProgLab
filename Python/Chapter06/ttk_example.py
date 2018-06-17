from tkinter import *
from tkinter.ttk import *


class ButtonArray(Frame):
	"""ttk.Buton の例"""

    def __init__(self,master=None):       
		"""コンストラクタ"""
        super().__init__(master)
        self['padding']=(20,20) 
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
		"""ウィジットの生成"""
        # スタイルの設定
        style = Style()
        style.configure('My.TButton', # ボタン
			font = ('Helveica', 12, 'bold'),
            foreground = 'yellow',
            background = 'blue')
        style.configure('My.TLabel', # ラベル
			font = ('Helveica', 12, 'italic'),
			anchor = 'center',
            foreground = 'green',
            background = 'white')
        # ボタン配列の生成
        buttons = [ [ Button(self, style='My.TButton') 
                            for icol in range(3) ] 
                            for irow in range(2) ]
        for irow in range(2):
            for icol in range(3):
				# 左クリック時の動作の登録
                buttons[irow][icol].bind('<Button-1>', self.press)
        # ボタン配列の配置
        for irow  in range(2):
            for icol in range(3):
                button = buttons[irow][icol]
                button['text'] = '({0},{1})'.format(irow,icol)
                button.grid(row=irow, column=icol)
        # ラベルの生成
        self.__var = StringVar()
        label = Label(self, style='My.TLabel')
        label.config(textvariable = self.__var)
        self.__var.set('(-,-)')
        label.grid(row=2, column=0, columnspan=3, sticky=(W,E))
        
        
    def press(self,event):
		"""ボタンクリックの動作"""
        self.__var.set(event.widget['text']) 
        
if __name__ == '__main__':
    
    root = Tk()
    root.title('ボタン')
    buttonArray = ButtonArray(root)
    root.mainloop()
    

