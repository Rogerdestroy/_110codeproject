import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd
#import pygame
import prettytable as pt
import random
import time
import sys
#from  moviepy.editor import *
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

a, b, c, d = 10, 100, 1000, 10000  #sells price
abuy, bbuy, cbuy, dbuy = 1, 1, 1, 1, #inport prise
a_num, b_num, c_num, d_num = 0, 0, 0, 0 #Purchase quantity
packet = 10000 #財產 
day = 0
power = 5 #體力
x, y = 0, 0


#數獨
def game_1():
    print('game_1()')
#井字遊戲
def game_2():
    print('game_2()')
#貪吃蛇
def game_3():
    print('game_3()')
#剪刀石頭布
def game_4():
    print('game_4()')

#button
def button_work():
    print('<<Work Today>>')
        
    global x #全域變數
    x = 1
  
    root.quit()
    root.destroy()
        
def button_play():
    print('<<Play Today>>')
    global x #全域變數
    x = 2
  
    root.quit()
    root.destroy()

def button_rest():
    print('<<Rest Today>>')
    global x #全域變數
    x = 3
  
    root.quit()
    root.destroy()
    
def button_end():
    print('====================================================\n')
    print('<<The End>>')
    global x #全域變數
    x = 4
  
    root.quit()
    root.destroy()

# play button
def callbackFunc(event):
     country = event.widget.get()
     print("開始"+country+"遊戲", end="")
     
     root.quit()
     root.destroy()

     line_day = "......"
     for x in line_day:
         print(x, end='')
         sys.stdout.flush()
         time.sleep(0.2)
     print('\n')
     
     global y #全域變數
     if country == 'Game_1':
         y = 1
         game_1()
     elif country == 'Game_2':
         y = 2
         game_2()
     elif country == 'Game_3':
         y = 3
         game_3()
     elif country == 'Game_4':
         y = 4
         game_4()

     
     
# main 
#第一個視窗
root = tk.Tk()
root.withdraw()
root.wm_attributes('-topmost',1) #至頂
messagebox.showinfo('Introduce', '這是一個有關創業的模擬器')
    
while True:
    
    '''
    
    遊戲狀況判斷
    
    '''
    #表格
    day += 1
    print("Day: ",day, '\t', "財產: ", packet , '\t', "體力： ", power)
        
    tb1 = pt.PrettyTable()
    tb1.field_names = ["Goods", "A", "B", "C", "D"]
    tb1.add_row(["Price", a, b, c, d])
    tb1.add_row(["Count", a_num, b_num, c_num, d_num])
    tb1.set_style(pt.DEFAULT)
    print(tb1)
    
  
    #等待
    time.sleep(0.5)
    
    #選擇事件視窗
    root = tk.Tk()
    root.title('Mine創業')
    root.geometry('540x540+500+200')
    root.wm_attributes('-topmost',1)
    
    mylabel = tk.Label(root, text='第'+str(day)+'天, 要做什麼?',font=('Arial', 30))
    #mylabel = tk.Label(root, text='今天要做什麼?',font=('Arial', 25))
    mylabel.pack()

    '''   
    x = str(input("你今天要做什麼?  "))
    #print(type(x))
    
    '''    

    mybutton = tk.Button(root, text='Work', height=4 , width=30, command=button_work , font=('Arial', 15))
    mybutton.pack()
    
    mybutton = tk.Button(root, text='Play', height=4 , width=30, command=button_play, font=('Arial', 15))
    mybutton.pack()
    
    mybutton = tk.Button(root, text='Rest', height=4 , width=30, command=button_rest, font=('Arial', 15))
    mybutton.pack()
    
    mybutton = tk.Button(root, text='End Game', height=4 , width=30, command=button_end, font=('Arial', 15))
    mybutton.pack()

    root.mainloop()
    
    #回來了
    #print(x)
    if x == 1: #開工
        print()
        
    elif x == 2:  #玩遊戲
        root = tk.Tk()
        root.title('Game')
        root.geometry('180x90+650+350')
        root.wm_attributes('-topmost',1)
        #ttk.Label(root, text = "Choose A Game", background = 'cyan', foreground ="black") 
        
        #labelTop = tk.Label(root, text = "Choose A Game")
        mycombobox = ttk.Combobox(root)
        mycombobox['values'] = ['Game_1','Game_2','Game_3','Game_4']
        mycombobox.pack(pady=30)
        mycombobox.current(0)
        
        mycombobox.grid(column = 1, row = 5) 
        mycombobox.current()
        mycombobox.bind("<<ComboboxSelected>>", callbackFunc)

        root.mainloop()
        #print(comboExample.current(), comboExample.get())
    
    elif x == 3: #休息
        print()
    
    elif x == 4: #結束遊戲
        break
    else:   #開工
        print()
    
    x = 0
    
    #clipVideo = VideoFileClip("car.gif")
    #clipVideo.write_gif("car.gif")
    
    '''
    
    結束天數判斷
    
    '''
    
    #time+sys 輸出文字
    line_day = "***恭喜妳過了第"+str(day)+"天***"
    for x in line_day:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)
    print('\n====================================================\n')
    #break #for test
    
#結算程式   
print("遊戲結算",end='')
line_day = "......"
for x in line_day:
    print(x, end='')
    sys.stdout.flush()
    time.sleep(0.2)
print('\n')