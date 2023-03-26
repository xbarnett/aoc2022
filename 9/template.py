from itertools import *
from math import *
from re import *
from utils import *

# findall(r"\d+", s)

def solve1(inp):
    inp = inp.strip().split("\n")
    k=[(0,0)]*2
    res = {(0,0)}
    for line in inp:
        d, n = line.split()
        n=int(n)
        for i in range(n):
            if d == "R":
                k[0] = (k[0][0]+1,k[0][1])
                for i in range(1,2):
                    if max(abs(k[i][0]-k[i-1][0]),abs(k[i][1]-k[i-1][1])) >= 2:
                        k[i] = s(k[i-1], k[i])
            if d == "L":
                k[0] = (k[0][0]-1,k[0][1])
                for i in range(1,2):
                    if max(abs(k[i][0]-k[i-1][0]),abs(k[i][1]-k[i-1][1])) >= 2:
                        k[i] = s(k[i-1], k[i])
            if d == "U":
                k[0] = (k[0][0],k[0][1]+1)
                for i in range(1,2):
                    if max(abs(k[i][0]-k[i-1][0]),abs(k[i][1]-k[i-1][1])) >= 2:
                        k[i] = s(k[i-1], k[i])
            if d == "D":
                k[0] = (k[0][0],k[0][1]-1)
                for i in range(1,2):
                    if max(abs(k[i][0]-k[i-1][0]),abs(k[i][1]-k[i-1][1])) >= 2:
                        k[i] = s(k[i-1], k[i])
            res.add(k[1])
    return len(res)

def s(h, t):
    m = 1000
    for i in range(-1,2):
        for j in range(-1,2):
            n = (t[0]+i,t[1]+j)
            d = abs(n[0]-h[0]) + abs(n[1]-h[1])
            if d < m:
                m = d
                r = n
    return r

def solve2(inp):
    inp = inp.strip().split("\n")
    k=[(0,0)]*10
    res = {(0,0)}
    for line in inp:
        d, n = line.split()
        n=int(n)
        for i in range(n):
            if d == "R":
                k[0] = (k[0][0]+1,k[0][1])
                for i in range(1,10):
                    if max(abs(k[i][0]-k[i-1][0]),abs(k[i][1]-k[i-1][1])) >= 2:
                        k[i] = s(k[i-1], k[i])
            if d == "L":
                k[0] = (k[0][0]-1,k[0][1])
                for i in range(1,10):
                    if max(abs(k[i][0]-k[i-1][0]),abs(k[i][1]-k[i-1][1])) >= 2:
                        k[i] = s(k[i-1], k[i])
            if d == "U":
                k[0] = (k[0][0],k[0][1]+1)
                for i in range(1,10):
                    if max(abs(k[i][0]-k[i-1][0]),abs(k[i][1]-k[i-1][1])) >= 2:
                        k[i] = s(k[i-1], k[i])
            if d == "D":
                k[0] = (k[0][0],k[0][1]-1)
                for i in range(1,10):
                    if max(abs(k[i][0]-k[i-1][0]),abs(k[i][1]-k[i-1][1])) >= 2:
                        k[i] = s(k[i-1], k[i])
            res.add(k[9])
    return len(res)

################################################################################
import pyperclip

main = solve2
real = True

test_input = r"""
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""

print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if real:
      pyperclip.copy(str(main(f.read())))
