import random
x=random.sample('1234567890',4)
print (x)
while True:
    y=input("輸入4個不同數字:")
    print (y)
    z = list(y)
    print (z)
    a=0
    for i in range(4):
        if x[i] is z[i]:
            a=a+1
    b=4-len(set(x)-set(z))-a
    print(a,"A", b, "B")
    if a == 4:
        break