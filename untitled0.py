import numpy as np
from math import log
import cv2
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

g = ["Goods", "A", "B", "C", "D"]
p = ["Price", "A", "B", "C", "D"]
c =["Count", "A", "B", "C", "D"]

tb1 = pt.PrettyTable()
tb1.field_names = g
tb1.add_row(p)
tb1.add_row(c)
tb1.set_style(pt.DEFAULT)
print(tb1)

g_tb = ["Goods"]
p_tb = ["Price"]
c_tb = ["Count"]