import tkinter as tk
import tkinter.ttk as ttk

def callbackFunc(event):
     print("New Element Selected")
     
app = tk.Tk() 
app.geometry('200x100')

labelTop = tk.Label(app,
                    text = "Choose your favourite month")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app, 
                            values=[
                                    "January", 
                                    "February",
                                    "March",
                                    "April"])

comboExample.grid(column=0, row=1)
comboExample.current(1)

comboExample.bind("<Button-2>", callbackFunc)

app.mainloop()