import random
class Customers_:
    def __init__(self, name, is_come, c_buy, d_buy):
        self.name = name
        self.is_come = is_come
        #self.a_buy = a_buy
        #self.b_buy = b_buy
        self.c_buy = c_buy
        self.d_buy = d_buy

data1 = [0,0,0,0,0.001]
data2 = [0,0,0,0,0,0,0,0,0,0.001]
customer = {}
i = 0

for i in range(10):        
    customer[i] = Customers_(i, 
                             bool(int(random.uniform(0,3))),
                             random.choice(data1),
                             random.choice(data2))
for i in range(10):    
    print(customer[i].name)
    print(customer[i].is_come)
    print(customer[i].c_buy)
    print(customer[i].d_buy)
    print('==========================')