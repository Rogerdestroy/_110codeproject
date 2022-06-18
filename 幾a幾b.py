import random
answer=random.sample('1234567890',4)
#print (answer)
while True:
    num=input("輸入4個不同數字:")
    #print (num)
    z = list(num)
    #print (z)
    a=0
    for i in range(4):
        if answer[i] is z[i]:
            a=a+1
    b=4-len(set(answer)-set(z))-a
    print(a,"A", b, "B")
    if a == 4:
        del a,b,answer,z,num
        break