import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pygame

#define 
long_design = 60  #框的長度
high_design = 10  #框的高度

#basic Variables 
a, b, c, d = 10, 100, 1000, 10000  #sells price
abuy, bbuy, cbuy, dbuy = 1, 1, 1, 1, #inport prise
a_num, b_num, c_num, d_num = 0, 0, 0, 0 #Purchase quantity
packet = 0 #財產

def out_line():
    for i in range(long_design):
        if i == long_design-1:
            print("=", end="\n")
        else:
            print("=", end="")
            
def out_avarge(title, str1, str2, str3, str4):
    e_ = len(title + str1 + str2 + str3 + str4)
    
    for i in range(long_design - e_ + 5):
        if i == 0:
            print("=",end="")
        elif i == long_design:
            print("=", end="\n")
        elif i == 1:
            print(title,end="")
        elif i == ((long_design-2)//5)*1 :
            print(str1,end="")
        elif i == ((long_design-2)//5)*2 :
            print(str2,end="")
        elif i == ((long_design-2)//5)*3 :
            print(str3,end="")
        elif i == ((long_design-2)//5)*4 :
            print(str4,end="")
        else:
            if i >= 6:
                print(" ",end="")
#開始
while True:
    out_line()#第一行
    '''
    for i in range(long_design): #第一行
        if i == long_design-1:
            print("=", end="\n")
        else:
            print("=", end="")
     
    '''
    
    for i in range(high_design): #中間行高
       if i == 2: #顯示貨物名稱
           out_avarge('貨物名稱', 'A', 'B', 'C', 'D')
       elif i == 4: #顯示目前價格
           out_avarge('目前價格', str(a), str(b), str(c), str(d))
       elif i== 6: #顯示剩餘數量
           out_avarge('剩餘數量', str(a_num), str(b_num), str(c_num), str(d_num))
       else: #過場
           for j in range(long_design):
              if j == 0 :
                  print("=",end="")
              elif j == long_design-1:
                  print("=",end="\n")
              else:
                  print(" ",end="")                
    
    
    '''
        for j in range(long_design-1):
            if j == 0 :
                print("=",end="")
            if j == long_design-2:
                print("=",end="\n")
                
            if 
            else:
                i ==2:
                if j == ((long_design-2)//5)*(1 or 2 or 3 or 4):
                    print("Z",end="")
                else:
                    print(" ",end="")
    '''
    
    out_line()#最後一行
    '''
    for i in range(long_design):    
        if i == long_design-1:
            print("=", end="\n")
        else:
            print("=", end="")
    '''
    break #for test
