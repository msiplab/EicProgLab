import tkinter as tk

class MyLabel(tk.Label):
    
    def __init__(self, msg):
        super().__init__(frame=None, 
                            text=msg, 
                            font=('Helvetica','24','bold'))

if __name__ == '__main__':
    label = MyLabel('Ciao, Mondo!')
    label.pack()
    label.mainloop()
