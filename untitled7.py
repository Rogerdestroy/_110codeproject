import random
customer = {}
class Customers_:
    def __init__(self, name, is_come, c_buy, d_buy):
        self.name = name
        self.is_come = is_come
        self.a_buy = 1
        self.b_buy = 1
        self.c_buy = c_buy
        self.d_buy = d_buy

for i in range(4):
    data1 = [0,0,0,0,0.001]
    data2 = [0,0,0,0,0,0,0,0,0,0.001]
            
    customer[i] = Customers_(i, 
                             #True if random.uniform(0,5) != 0 else False
                             bool(int(random.uniform(0,3))),
                             random.choice(data1),
                             random.choice(data2))
    del data1, data2

for i in range(4):
    print(customer[i].name)
    print(customer[i].is_come)
    print(customer[i].a_buy)
    print(customer[i].b_buy) 
    print(customer[i].c_buy)
    print(customer[i].d_buy)
print('===================================')


customer[0].is_come = 0
customer[0].a_buy *= 0.9
customer[0].d_buy *= 10

for i in range(1):
    print(customer[i].name)
    print(customer[i].is_come)
    print(customer[i].a_buy)
    print(customer[i].b_buy) 
    print(customer[i].c_buy)
    print(customer[i].d_buy)