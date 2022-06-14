import numpy as np
from math import log
import cv2
#import matplotlib.pyplot as plt
#import pandas as pd
#import pygame
import prettytable as pt
import random
import time
import sys
#from  moviepy.editor import *
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
#import wx
   
a, b, c, d = 10, 100, 1000, 10000  #sells price
abuy, bbuy, cbuy, dbuy = 1, 1, 1, 1, #import prise
a_num, b_num, c_num, d_num = 0, 0, 0, 0 #Purchase quantity

packet = 10000 #財產 
day = 0
power = 5 #體力
x, y = 0, 0 #按鈕編號
cus = 0 #顧客
customer = {} #顧客性質儲存
year_c, month_c, day_c, week_c = 2000, 1, 1, 6
#g_tb = ['Goods','Pen','Food','Hat','Jewelry']
p_tb = ["Price",0,0,0,0]
c_tb = ["Count",0,0,0,0]

class Customers_:
    def __init__(self, name, is_come, c_buy, d_buy):
        self.name = name
        self.is_come = is_come
        #self.a_buy = a_buy
        #self.b_buy = b_buy
        self.c_buy = c_buy
        self.d_buy = d_buy

class Goods_:
    def __init__(self, name, num, in_prise, willbuy, frequency, alternatives):
        #名稱, 數量, 進貨價格, 進店後購買率, 購買平率(幾天買一次), 替代商品造成影響
        self.name = name
        self.num = num
        self.in_prise = in_prise 
        self.wiilbuy = willbuy
        self.frequency = frequency
        self.alternatives = alternatives 
        
class Store(): 
    #顧客數量
    def customer_n(cus,day):  #潛在客戶(知道有這間店的人)
        if day > 50 or cus > 1000:
            return cus +  random.randint(0,3)
        elif day<30:
            return cus +  random.randint(0, int(log(day+1, 2.2)))
        else:
            return cus +  random.randint(0, int(log(day+1, 2)))
        
    def customer_come(day, weather, ): #會進商店的顧客
        print()
    
    #inventory_cost 存貨成本
    def storehouse():   #存貨倉庫
        print()
    def interest():     #銀行利息
        print()
    
    #def 
    
    # ordering_cost 物品成本
    def order_cost():   #物品成本
        print()
        
    def truck():        #運送成本 
        print()
    
    #shortage_cost 短缺商譽損失
    def compensation(): #賠償
        print()
    def ctmlose_shortage():  #顧客損失
        print()


class Control_: 
    
    def exit_tk():
        root.quit()
        root.destroy()
        
    def print_one(line_todo):
        for x in line_todo:
             print(x, end='')
             sys.stdout.flush()
             time.sleep(0.15)
                 
    def clock():
        global year_c, month_c, day_c, week_c
        print(str(year_c)+'年 \t'+str(month_c)+'月\t'+str(day_c)+'日\t'+' 星期'+str(week_c))
        
        #時間計算
        leap_year = 0
        m31 = ['1', '3', '5', '7', '8', '10', '12']
        m30 = ['4', '6', '9', '11']
        if year_c % 4 == 0 and year_c % 100 != 0:
            leap_year = 1
        elif year_c % 4 == 0 and year_c % 100 == 0 and year_c % 400==0:
            leap_year = 1
        else:
            leap_year = 0
        
        if week_c == 7:
            week_c = 1
        else:
            week_c += 1
        
        day_c += 1
        
        
        if day_c > 28 and  leap_year == 0 and month_c == 2:
            month_c += 1
            day_c = 1
        elif day_c > 29 and  leap_year == 1 and month_c == 2:
            month_c += 1
            day_c = 1
        elif day_c>30 and str(month_c) in m30:
            month_c += 1
            day_c = 1
        elif day_c>31 and str(month_c) in m31:
            if month_c == 12:
                month_c = 1
                day_c = 1
                year_c += 1
            else:
                month_c += 1
                day_c = 1
    
    def tb_add(a, b, c):
        pass 
    
    def tb_(a, b, c):
        pass

class Button_work():
   
    def createNewWindow():
        newWindow = tk.Toplevel(root)
        labelExample = tk.Label(newWindow, text = "New Window")
        buttonExample = tk.Button(newWindow, text = "New Window button")
    
        labelExample.pack()
        buttonExample.pack()
    
def Work_():
    #Button_work.createNewWindow()
    pass
    
class game_1():
      
    def drawBoard_():
    
        print("數字鍵對應位置")
        print(" " + "7" + " | " + "8" + " | " + '9')
        print("------------")
        print(" " + '4' + " | " + '5' + " | " + '6')
        print("------------")
        print(" " + '1' + " | " + '2' + " | " + '3')
        print('\n')

    def drawBoard(board):
    
        print(" " + board[7] + " | " + board[8] + " | " + board[9])
        print("------------")
        print(" " + board[4] + " | " + board[5] + " | " + board[6])
        print("------------")
        print(" " + board[1] + " | " + board[2] + " | " + board[3])
    
    # 玩家選擇所想用的棋子種類
    def inputPlayerLetter() :
    
        letter = ''
        while not (letter == 'X' or letter == 'O') :
            print("你要 \'x\' 還是 \'o\' ？",end='\n')
            # 自動將小寫轉化為大寫
            letter = input().upper()
    
        # 如果玩家選擇的X，則自動將O賦給電腦，反之一樣
        if letter == 'x' :
            return ['x','o']
        else :
            return ['o','x']
    
    # 這裡隨機生成0或者1來表示誰先落子
    def whoGoesFirst() :
    
        if random.randint(0,1) == 0 :
            return 'computer'
        else :
            return 'player'
    
    # 如果玩家選擇y或者Y則遊戲重新開始
    #def playAgain():
    
    #    print("Do you want to play again?(yes or no)")
    #    return input().lower().startswith('y')
    
    # 將棋子放置到棋盤上面
    # board引數是儲存棋子的列表
    # letter引數是棋子的型別
    # move是選擇將棋子放在哪
    def makeMove(board, letter, move) :
    
        board[move] = letter
    
    #  根據井字棋規則判斷是否獲勝
    def isWinner(bo, le) :
    
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or
                (bo[4] == le and bo[5] == le and bo[6] == le) or
                (bo[1] == le and bo[2] == le and bo[3] == le) or
                (bo[7] == le and bo[4] == le and bo[1] == le) or
                (bo[8] == le and bo[5] == le and bo[2] == le) or
                (bo[9] == le and bo[6] == le and bo[3] == le) or
                (bo[7] == le and bo[5] == le and bo[3] == le) or
                (bo[9] == le and bo[5] == le and bo[1] == le))
    
    # 將已經在棋盤上的棋子備份,隨時更新
    def getBoardCopy(board) :
    
        dupeBoard = []
        for i in board :
            dupeBoard.append(i)
    
        return dupeBoard
    
    # 判斷棋盤是否還有可落子的地方
    def isSpaceFree(board, move) :
    
        return board[move] == ' '
    
    # 獲取玩家落子的位置
    def getPlayerMove(board) :
    
        move = ' '
        # 判斷落子的位置是否正確以及棋盤是否還能落子
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not game_1.isSpaceFree(board, int(move)) :
    
            print("What is your next move?(1-9)")
            move = input()
        return int(move)
    
    # 找到可以落子的地方，主要是計算機使用的
    def chooseRandomMoveFromList(board, moveList) :
    
        possibleMoves = []
        for i in moveList :
            if game_1.isSpaceFree(board, i) :
                possibleMoves.append(i)
    
        if len(possibleMoves) != 0 :
            return random.choice(possibleMoves)
        else :
            return None
        
    def getComputerMove(board, computerLetter) :
    
        # 給出棋盤上電腦和玩家棋子的型別
        if computerLetter == 'X' :
            playerLetter = 'O'
        else :
            playerLetter = 'X'
    
        for i in range(1,10) :
            # 在備份的棋盤中判斷是否有可以落子的地方
            copy = game_1.getBoardCopy(board)
            if game_1.isSpaceFree(copy, i) :
                # 如果有可以落子的地方,則先在備份的棋盤上落子
                game_1.makeMove(copy, computerLetter, i)
                # 落子後判斷電腦是否能贏,並且返回能贏的落子的位置
                if game_1.isWinner(copy, computerLetter) :
                    return i
    
        for i in range(1,10) :
            copy = game_1.getBoardCopy(board)
            if game_1.isSpaceFree(copy, i) :
                # 在備份的棋盤上模擬玩家落子
                game_1.makeMove(copy, playerLetter, i)
                # 如果下一次玩家落子就可以贏,返回玩家落子的位置,用於堵住玩家
                if game_1.isWinner(copy, playerLetter) :
                    return i
    
        # 隨機在四個角處落子
        move = game_1.chooseRandomMoveFromList(board,[1,3,7,9])
        if move != None :
            return move
    
        # 如果角處已被佔滿,則落子在中間位置5處
        if game_1.isSpaceFree(board, 5) :
            return 5
    
        # 如果角和中間都被佔滿,則隨機選擇邊上落子
        return game_1.chooseRandomMoveFromList(board,[2,4,6,8])
    
    # 判斷棋盤是否已滿
    def isBoardFull(board) :
    
        for i in range(1,10) :
            if game_1.isSpaceFree(board, i) :
                return False
        return True
    

class Game_:

    #井字遊戲
    def game_1():
        #print('game_1')
        print("\nWelcome to 井字遊戲 !!!")
        
        game_WWGG = 0 #分數
        
        for i in range(3):
            print("第 "+str(i+1)+' 場遊戲 , 共 3 場')
            # 初始化棋盤為空
            theBoard = [' '] * 10
            # 玩家和電腦棋子型別的選擇
            playerLetter, computerLetter = game_1.inputPlayerLetter()
           
            # 範例 
            game_1.drawBoard_() 
           
            # 先後順序的決定
            turn = game_1.whoGoesFirst()
            print(' \''+ turn + '\'會先執行')
            
            # 遊戲開始的標誌位,當遊戲結束時變成False
            game_1.gameIsPlaying = True
            
            
            
            while game_1.gameIsPlaying :
                # 玩家先行
                if turn == 'player' :
                    game_1.drawBoard(theBoard)
                    # 獲取玩家下棋的位置
                    move = game_1.getPlayerMove(theBoard)
                    # 將玩家的棋子傳入列表相應的位置
                    game_1.makeMove(theBoard, playerLetter, move)
        
                    # 如果玩家獲勝,標誌位變為False
                    if game_1.isWinner(theBoard, playerLetter) :
                        game_1.drawBoard(theBoard)
                        print("You win !")
                        game_WWGG += 1
                        game_1.gameIsPlaying = False
                    # 否則則判斷棋盤是否已滿
                    else :
                        if game_1.isBoardFull(theBoard) :
                            game_1.drawBoard(theBoard)
                            print("Tie")
                            game_WWGG += 0.5
                            break
                        # 若棋盤未滿,且玩家已落子,則下一次落到計算機落子
                        else :
                            turn = 'computer'
                # 電腦先行
                else :
                    # 電腦隨機選擇位置落子
                    move = game_1.getComputerMove(theBoard, computerLetter)
                    game_1.makeMove(theBoard, computerLetter, move)
        
                    # 如果電腦落子獲勝,則遊戲結束
                    if game_1.isWinner(theBoard, computerLetter) :
                        game_1.drawBoard(theBoard)
                        print("You lose !")
                        game_1.gameIsPlaying = False
                    else :
                        if game_1.isBoardFull(theBoard) :
                            game_1.drawBoard(theBoard)
                            print("Tie")
                            break
                        else :
                            turn = 'player'
        
            # 玩家沒有再次開始遊戲,則跳出迴圈
            #if not game_1.playAgain():
            #    break
        global power
        if game_WWGG >= 2:
            
            power += 2
        elif game_WWGG == 1.5:
            
            power += 1
        elif game_WWGG < 1.5:
            
            power -= 1
            
    #剪刀石頭布
    def game_2():
        print('麻煩請玩遊戲 1') #random???
        Control_.print_one('更換遊戲中.......\n')
        Game_.game_1()
    #貪吃蛇
    def game_3():
        print('麻煩請玩遊戲 1') #random???
        Control_.print_one('更換遊戲中.......\n')
        Game_.game_1()
    #數獨
    def game_4(): 
        print('麻煩請玩遊戲 1') #random???
        Control_.print_one('更換遊戲中.......\n')
        Game_.game_1()


#button
class button_main():
    def button_work():
        print('<<Work Today>>')
            
        global x #全域變數
        x = 1
      
        Control_.exit_tk()
            
    def button_play():
        print('<<Play Today>>')
        global x #全域變數
        x = 2
      
        Control_.exit_tk()
    
    def button_rest():
        print('<<Rest Today>>')
        global x #全域變數
        x = 3
      
        Control_.exit_tk()
        
    def button_end():
        print('====================================================\n')
        print('<<The End>>')
        global x #全域變數
        x = 4
      
        Control_.exit_tk()

# play button
def callbackFunc(event):
     country = event.widget.get()
     print("開始"+country+"遊戲", end="")
     
     Control_.exit_tk()
     
     '''
     root.quit()
     root.destroy()
     '''
     Control_.print_one("......\n")
     '''
     line_day = "......"
     for x in line_day:
         print(x, end='')
         sys.stdout.flush()
         time.sleep(0.2)
     '''
     #print('\n')
    
     
     global y #全域變數
     if country == 'Game_1':
         y = 1
         Game_.game_1()
     elif country == 'Game_2':
         y = 2
         Game_.game_2()
     elif country == 'Game_3':
         y = 3
         Game_.game_3()
     elif country == 'Game_4':
         y = 4
         Game_.game_4()

class Draw_:
    
    def draw_random():
     
        # 1.创建白色背景图片
        d = 200
        img = np.ones((d, d, 3), np.uint8) * 255
     
        # 2.循环随机绘制实心圆
        for i in range(0, 100):
            # 随机中心点
            center_x = np.random.randint(0, high=d)
            center_y = np.random.randint(0, high=d)
     
            # 随机半径与颜色
            radius = np.random.randint(5, high=d/5)
            color = np.random.randint(0, high=256, size=(3, )).tolist()
     
            cv2.circle(img, (center_x, center_y), radius, color, -1)
     
        # 3.显示结果
        cv2.imshow("img", img)
        cv2.waitKey()
        cv2.destroyAllWindows()    
     
# main 
if __name__ == "__main__":
    #第一個視窗
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes('-topmost',1) #至頂
    messagebox.showinfo('Introduce', '這是一個有關創業的模擬器')
        
    while True:
        
        '''
        
        遊戲狀況判斷
        
        '''
        if power <= 0 or packet <= 0:
            break
        
        #來客數
        tmp = cus
        cus = Store.customer_n(cus, day)
        #print(cus)
        
        #顧客性質
        for i in range(tmp,cus):
            data1 = [0,0,0,0,0.001]
            data2 = [0,0,0,0,0,0,0,0,0,0.001]
            
            customer[i] = Customers_(i, 
                                   #True if random.uniform(0,5) != 0 else False
                                   bool(int(random.uniform(0,3))),
                                   random.choice(data1),
                                   random.choice(data2))
            del data1, data2
        del tmp  
        
        '''
        for i in range(cus):
            print(customer[i].name)
            print(customer[i].is_come)
            print(customer[i].c_buy)
            print(customer[i].d_buy)
        '''
        
        #日期
        Control_.clock()
        
        #表格
        day += 1
        print("Day: ",day, '\t', "財產: ", packet , '\t', "體力： ", power)
        
        #g_tb = ["Goods"]
        #p_tb = ["Price"]
        #c_tb = ["Count"]

        tb1 = pt.PrettyTable()
        tb1.field_names = ['Goods','Pen','Food','Hat','Jewelry']
        tb1.add_row(p_tb)
        tb1.add_row(c_tb)
        tb1.set_style(pt.DEFAULT)
        print(tb1)
        
        print('')
      
        #等待
        time.sleep(0.5)
        
        #選擇事件視窗
        root = tk.Tk()
        root.title('Mine創業')
        root.geometry('540x540+350+180')
        root.wm_attributes('-topmost',1)
        
        mylabel = tk.Label(root, text='第'+str(day)+'天, 要做什麼?',font=('Arial', 30))
        #mylabel = tk.Label(root, text='今天要做什麼?',font=('Arial', 25))
        mylabel.pack()
    
        '''   
        x = str(input("你今天要做什麼?  "))
        #print(type(x))
        
        '''    
    
        mybutton = tk.Button(root, text='Work', height=4 , width=30, command=button_main.button_work , font=('Arial', 15))
        mybutton.pack()
        
        mybutton = tk.Button(root, text='Play', height=4 , width=30, command=button_main.button_play, font=('Arial', 15))
        mybutton.pack()
        
        mybutton = tk.Button(root, text='Rest', height=4 , width=30, command=button_main.button_rest, font=('Arial', 15))
        mybutton.pack()
        
        mybutton = tk.Button(root, text='End Game', height=4 , width=30, command=button_main.button_end, font=('Arial', 15))
        mybutton.pack()
    
        root.mainloop()
        
        #回來了
        #print(x)
        if x == 1: #開工
            Work_()
            
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
            
            Control_.print_one('又是耍廢的一天呢~~~\n')
            #print('又是耍廢的一天呢~~~')
            #print('\n')
            Draw_.draw_random()
            
        elif x == 4: #結束遊戲
            break
        
        else:   #開工
            Work_()
        
        x = 0
        
        #clipVideo = VideoFileClip("car.gif")
        #clipVideo.write_gif("car.gif")
        
        '''
        
        結束天數判斷
        
        '''
        
        #time+sys 輸出文字
        Control_.print_one("***恭喜妳過了第"+str(day)+"天***")
        '''
        line_day = "***恭喜妳過了第"+str(day)+"天***"
        for x in line_day:
            print(x, end='')
            sys.stdout.flush()
            time.sleep(0.1)
        '''
        print('\n====================================================\n')
        #break #for test
    
#結算程式   
print("遊戲結算",end='')
Control_.print_one("......")
'''
line_day = "......"
for x in line_day:
    print(x, end='')
    sys.stdout.flush()
    time.sleep(0.2)
'''
print('\n')
if power <= 0 or packet <= 0:
    print(
    '''
    \ \   / /          | |
     \ \_/ /__  _   _  | |       _____ ___
      \   / _ \| | | | | |/ _ \ / ___// _ \ 
       | | (_) | |_| | | | (_) (__  )/  __/
       |_|\___/ \__,_| |_|\___/____/ \___/ you lose...
    '''
    )

    #os._exit()
else:
    print()
    
print(
'''
  _____ __                __
 /_  __/ /_  ____  ____  / /__  ____
  / / / __ \/ __ \/ __ \/ // // ___/
 / / / / / / /_/ / / / / , < (__  )
/_/ /_/ /_/\__,_/_/ /_/_/|_|/____/ 
'''
)

sys.exit(0)