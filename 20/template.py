from itertools import *
from math import *
from re import *
from utils import *
from networkx import *

# findall(r"\d+", s)

def solve1(inp):
    inp = inp.strip().split("\n")
    z = []
    for i,x in enumerate(inp):
        z.append((i, int(x)))
    n = len(z)
    for i in range(n):
        print("stage",i)
        for j,(k,x) in enumerate(z):
            if k == i:
                break
        k = (j+x-1)%(n-1)+1
        if j < k:
            z = z[:j] + z[j+1:k+1] + [z[j]] + z[k+1:]
        elif j > k:
            z = z[:k] + [z[j]] + z[k:j] + z[j+1:]
    for i,(_,x) in enumerate(z):
        if x == 0:
            break
    r = 0
    for j in [1000,2000,3000]:
        r += z[(i+j)%n][1]
    return r
        

def solve2(inp):
    inp = inp.strip().split("\n")
    z = []
    for i,x in enumerate(inp):
        z.append((i, int(x)*811589153))
    n = len(z)
    for l in range(10):
        for i in range(n):
            for j,(k,x) in enumerate(z):
                if k == i:
                    break
            k = (j+x-1)%(n-1)+1
            if j < k:
                z = z[:j] + z[j+1:k+1] + [z[j]] + z[k+1:]
            elif j > k:
                z = z[:k] + [z[j]] + z[k:j] + z[j+1:]
    for i,(_,x) in enumerate(z):
        if x == 0:
            break
    r = 0
    for j in [1000,2000,3000]:
        r += z[(i+j)%n][1]
    return r

################################################################################
import pyperclip

main = solve2
real = True

test_input = r"""
1
2
-3
3
-2
0
4
"""

print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if real:
        sol = main(f.read())
        print(sol)
        pyperclip.copy(str(sol))
