from itertools import *
from math import *
from re import *
from utils import *
from networkx import *
import time
# findall(r"\d+", s)

def solve1(inp):
    inp = inp.strip().split("\n")
    z = {}
    m = -10000000000000000 # highest y coord
    for line in inp:
        v = line.split(" -> ")
        for i in range(len(v)-1):
            x0,y0=v[i].split(",")
            x1,y1=v[i+1].split(",")
            x0=int(x0)
            x1=int(x1)
            y0=int(y0)
            y1=int(y1)
            if x0 == x1:
                for j in range(min(y0,y1),max(y0,y1)+1):
                    z[(x0,j)] = "w"
            else:
                for j in range(min(x0,x1),max(x0,x1)+1):
                    z[(j,y0)] = "w"

            m=max(m,y0,y1)
    s = (500,0)
    r = 0
    while True:
        g = s
        b = False
        while g not in z:
            if g[1] == m+1:
                break
            elif (g[0],g[1]+1) not in z:
                g=(g[0],g[1]+1)
            elif (g[0]-1,g[1]+1) not in z:
                g=(g[0]-1,g[1]+1)
            elif (g[0]+1,g[1]+1) not in z:
                g=(g[0]+1,g[1]+1)
            elif g == s:
                b = True
                break
            else:
                break
        z[g]="s"
        r += 1
        if b:
            break
    return r

            
            

def solve2(inp):
    inp = inp.strip().split("\n")
    return inp

################################################################################
import pyperclip

main = solve1
real = True

test_input = r"""
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if real:
        t0 = time.time()
        sol = main(f.read())
        t1 = time.time()
        print(sol)
        print(t1-t0)
        pyperclip.copy(str(sol))
