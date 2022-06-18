def initialize(): 
    global gnum 
    gnum = 1
    
def add():
    global gnum 
    global_var.gnum += 1

def add2():
    global gnum 
    global_var.gnum += 2

def d1():
    global gnum 
    global_var.gnum -= 1
    
def print_():
    print(gnum)