from tkinter import *
from tkinter.font import Font

def main(): 
    # ウィンドウのルート設定
    root = Tk()
    root.title('タイトル')
    root.geometry('240x30')
    
    # ルートへのラベルウィジットの生成
    myfont = Font(size=20)    
    label = Label(root,text='GUIプログラム例', font=myfont)
    
    # ウイジットの設置
    label.pack()
    
    # メインループ
    root.mainloop()

if __name__ == '__main__':
    main()
    
