from matrix import *
from draw import *
from display import *
from parse import *
import math
import random

s = new_screen()
c = [ 255, 192, 203 ]
zbuffer = new_buffer()

edges = [[], [], [], []]
triangles = [[], [], [], []]
m = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
cs = [m]


parse('script', edges, triangles, cs, s, c, zbuffer)
