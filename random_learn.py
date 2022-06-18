import random
random.choice([1, 2, 3])

#取兩個
random.sample([1, 2, 3, 4],2)

data=[0,1,5,8]
#調換資料順序
random.shuffle(data)

#0~1隨機亂數
random.random()

#機率相同
random.uniform(1,10)

#常態分配亂數 , 平均100 ,標準差10
random.normalvariate(100, 10)
#while True:
    
    print()
    print(random.choice([0,0,0,0,0.001]),random.choice([0,0,0,0,0,0,0,0,0,0,0.001]))
    
#while True:
data1 = [0,0,0,0,0.001]
data2 = [0,0,0,0,0,0,0,0,0,0.001]   
    print()
    print(random.choice([data1]),random.choice([data1]))