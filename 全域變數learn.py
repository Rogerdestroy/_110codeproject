import global_var
import os
import sys
  
global_var.initialize() 
print( global_var.gnum )

os.system("start /wait  python app1.py")

global_var.print_()
