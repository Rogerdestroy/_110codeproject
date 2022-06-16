import tkinter as tk

def createNewWindow():
    newWindow = tk.Toplevel(root)
    labelExample = tk.Label(newWindow, text = "New Window")
    buttonExample = tk.Button(newWindow, text = "New Window button")

    labelExample.pack()
    buttonExample.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Mine創業')
    root.geometry('540x540+350+180')
    root.wm_attributes('-topmost',1)
    
    mybutton = tk.Button(root, text='Work', height=4 , width=30, 
                         command=createNewWindow, 
                         font=('Arial', 15))
    mybutton.pack()
    root.wm_attributes('-topmost',0)
    root.mainloop()