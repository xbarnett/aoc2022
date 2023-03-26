from itertools import *
from math import *
from re import *
from utils import *
from networkx import *

# findall(r"\d+", s)

t = [[(0,0),(1,0),(2,0),(3,0)],
     [(0,1),(1,0),(1,1),(1,2),(2,1)],
     [(0,0),(1,0),(2,0),(2,1),(2,2)],
     [(0,0),(0,1),(0,2),(0,3)],
     [(0,0),(0,1),(1,0),(1,1)]]

def good(z,p,x,y):
    for (x0,y0) in p:
        if not (0 <= x + x0 <= 6):
            return False
        if not (y + y0 >= 0):
            return False
        if (x+x0,y+y0) in z:
            return False
    return True

def pri(z,h):
    for y in range(h,-1,-1):
        for x in range(7):
            if (x,y) in z:
                print("#",end="")
            else:
                print(".",end="")
        print()

def prit(z,h):
    for y in range(h,h-10,-1):
        for x in range(7):
            if (x,y) in z:
                print("#",end="")
            else:
                print(".",end="")
        print()
    print(h)
    print()


def top(z,h):
    res = set()
    for y in range(h,h-50,-1):
        for x in range(7):
            if (x,y) in z:
                res.add((x,h-y))
    return res

def solve1(inp):
    inp = inp.strip().split("\n")[0]
    i = 0
    c = 0
    z = set()
    h = 0
    y = 3
    x = 2
    while True:
        #print(x,y,z)
        d = inp[i%(len(inp))]
        i += 1
        if d==">" and good(z,t[c%(len(t))],x+1,y):
            x+=1
        if d=="<" and good(z,t[c%(len(t))],x-1,y):
            x -= 1
        if good(z,t[c%(len(t))],x,y-1):
            y -= 1
        else:
            for (x0,y0) in t[c%(len(t))]:
                z.add((x+x0,y+y0))
                h=max(h,y+y0)
            c += 1
            y = 4+h
            x = 2
            #pri(z,h)
            #print()
        if c == 2022:
            return h+1
        

def solve2(inp):
    inp = inp.strip().split("\n")[0]
    i = 0
    c = 0
    z = set()
    h = 0
    y = 3
    x = 2
    per = 1715
    tops = []
    n = 1000000000000
    c1 = 11716
    h1 = 18552
    c8 = 13431
    h8 = 21263
    cycles = (n-c1)//(c8-c1)
    result = h1 + cycles*(h8-h1)
    remaining = (n-c1)%(c8-c1)
    while True:
        #print(x,y,z)
        d = inp[i%(len(inp))]
        i += 1
        if d==">" and good(z,t[c%(len(t))],x+1,y):
            x+=1
        if d=="<" and good(z,t[c%(len(t))],x-1,y):
            x -= 1
        if good(z,t[c%(len(t))],x,y-1):
            y -= 1
        else:
            for (x0,y0) in t[c%(len(t))]:
                z.add((x+x0,y+y0))
                h=max(h,y+y0)
            c += 1
            y = 4+h
            x = 2
            if c == remaining+c1:
                return result+h-h1+1
##            if True:
##                tops.append((c, h, top(z,h)))
            if c == 11716:
                c1 = c
                h1 = h
            if c == 11716+1715:
                c8 = c
                h8 = h
##            if c % 100 == 0:
##                print("status", c)
            if c == 20000:
                break
##    for (c,h,s) in tops[1000:]:
##        if tops[1000][2] == s:
##            print(c,h)
    print(c1,h1,c8,h8)
        

################################################################################
import pyperclip

main = solve2
real = True

test_input = r"""
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
"""

#print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if real:
        sol = main(f.read())
        print(sol)
        pyperclip.copy(str(sol))
