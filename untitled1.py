import tkinter as tk
import tkinter.ttk as ttk
 
root = tk.Tk()
root.title('my window')
root.geometry('540x540')

mycombobox = ttk.Combobox(root)
mycombobox['values'] = ['apple','banana','orange','lemon','tomato']
mycombobox.pack(pady=30)
mycombobox.current(0)

root.mainloop()