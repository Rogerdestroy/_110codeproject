import tkinter as tk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.title('hello world')
        self.geometry('200x150')

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()