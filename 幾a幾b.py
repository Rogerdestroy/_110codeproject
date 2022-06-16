import random
x=random.sample('1234567890',4)
print (x)
while True:
    y = input("輸入4個不同數字:")
    print (y)
    z = list(y)
    print (z)
    for i in range(4):
            if x[i] == num[1]:
                a += 1
    b = 4-len(set(x)-set(z))-a
    print(a,"A", b, "B")
    if a == 4:
        break