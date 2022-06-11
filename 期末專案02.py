#import numpy as np
#import cv2
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
import wx

a, b, c, d = 10, 100, 1000, 10000  #sells price
abuy, bbuy, cbuy, dbuy = 1, 1, 1, 1, #inport prise
a_num, b_num, c_num, d_num = 0, 0, 0, 0 #Purchase quantity
packet = 10000 #財產 
day = 0
power = 5 #體力
x, y = 0, 0
game_ff = ''

class Cournet_:
    
    def exit_tk():
        root.quit()
        root.destroy()

def game_1():
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
            print("你要 \'x\' 還是 \'o\' ？")
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
    def playAgain():
    
        print("Do you want to play again?(yes or no)")
        return input().lower().startswith('y')
    
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
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)) :
    
            print("What is your next move?(1-9)")
            move = input()
        return int(move)
    
    # 找到可以落子的地方，主要是計算機使用的
    def chooseRandomMoveFromList(board, moveList) :
    
        possibleMoves = []
        for i in moveList :
            if isSpaceFree(board, i) :
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
            copy = getBoardCopy(board)
            if isSpaceFree(copy, i) :
                # 如果有可以落子的地方,則先在備份的棋盤上落子
                makeMove(copy, computerLetter, i)
                # 落子後判斷電腦是否能贏,並且返回能贏的落子的位置
                if isWinner(copy, computerLetter) :
                    return i
    
        for i in range(1,10) :
            copy = getBoardCopy(board)
            if isSpaceFree(copy, i) :
                # 在備份的棋盤上模擬玩家落子
                makeMove(copy, playerLetter, i)
                # 如果下一次玩家落子就可以贏,返回玩家落子的位置,用於堵住玩家
                if isWinner(copy, playerLetter) :
                    return i
    
        # 隨機在四個角處落子
        move = chooseRandomMoveFromList(board,[1,3,7,9])
        if move != None :
            return move
    
        # 如果角處已被佔滿,則落子在中間位置5處
        if isSpaceFree(board, 5) :
            return 5
    
        # 如果角和中間都被佔滿,則隨機選擇邊上落子
        return chooseRandomMoveFromList(board,[2,4,6,8])
    
    # 判斷棋盤是否已滿
    def isBoardFull(board) :
    
        for i in range(1,10) :
            if isSpaceFree(board, i) :
                return False
        return True
    

class Game_:

    #井字遊戲
    def game_1():
        print('game_1()')
        print("Welcome to 井字遊戲 !!!")

        for i in range(3):
        
            # 初始化棋盤為空
            theBoard = [' '] * 10
            # 玩家和電腦棋子型別的選擇
            playerLetter, computerLetter = game_1.inputPlayerLetter()
           
            # 範例 
            game_1.drawBoard_() 
           
            # 先後順序的決定
            turn = game_1.whoGoesFirst()
            print('The ' + turn + ' will go first')
            
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
                        game_1.gameIsPlaying = False
                    # 否則則判斷棋盤是否已滿
                    else :
                        if game_1.isBoardFull(theBoard) :
                            game_1.drawBoard(theBoard)
                            print("Tie")
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
            if not game_1.playAgain():
                break
        
    #剪刀石頭布
    def game_2():
        print('game_2()')
    #貪吃蛇
    def game_3():
        print('game_3()')
    #數獨
    def game_4():
        print('game_4()')


#button
def button_work():
    print('<<Work Today>>')
        
    global x #全域變數
    x = 1
  
    Cournet_.exit_tk()
        
def button_play():
    print('<<Play Today>>')
    global x #全域變數
    x = 2
  
    Cournet_.exit_tk()

def button_rest():
    print('<<Rest Today>>')
    global x #全域變數
    x = 3
  
    Cournet_.exit_tk()
    
def button_end():
    print('====================================================\n')
    print('<<The End>>')
    global x #全域變數
    x = 4
  
    Cournet_.exit_tk()

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
            mycombobox.current()
            
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