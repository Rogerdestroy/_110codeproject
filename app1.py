import global_var
import random

print("\nWelcome to 幾A幾B !!!")
ti = 0
answer=random.sample('1234567890',4)
print (answer)

while True:
    num=input("輸入4個不同數字:")
    ti += 1
    print (num)
    z = list(num)
    print (z)
    a = 0
    for i in range(4):
        if answer[i] is z[i]:
            a = a+1
            b = 4-len(set(answer)-set(z))-a
    print(a,"A", b, "B")
   
    if a == 4:
        if ti >8:
            print('你好爛... 共猜了'+str(ti)+'次')
            global_var.d1()
            
        elif ti<=8 and ti>4:
            print('不錯~ 共猜了'+str(ti)+'次')
            global_var.add()
            
        elif ti<=4 and ti>0:
            print('超級強!  共猜了'+str(ti)+'次')
            global_var.add2()
            
        del a,b,answer,z,num,ti
        break
        
    elif str(num) == 'sos':
        print('退出遊戲...')
        #global power
        global_var.d1()
        break
