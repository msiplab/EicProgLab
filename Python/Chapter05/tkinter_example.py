import tkinter as tk

class MyLabel(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self)
        self.label['text'] = 'Ciao, Mondo!'
        self.label['font'] = ('Helvetica','24','bold')
        self.label.pack()

if __name__ == '__main__':
    root = tk.Tk()
    mylabel = MyLabel(root)
    mylabel.mainloop()
    

