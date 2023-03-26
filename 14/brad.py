from itertools import *
from math import *
from re import *
from utils import *
from networkx import *
import time
# findall(r"\d+", s)

def solve1(inp):
    data = inp.strip().split("\n")
    s = set()

    for i in data:
        r = [tuple(map(int, j.split(","))) for j in i.split(" -> ")]
        for j in range(1, len(r)):
            p, q = sorted(r[j-1:j+1])
            s.update((x,y) for x in range(p[0], q[0]+1) for y in range(p[1], q[1]+1))

    y = max(g[1] for g in s)
    n = len(s)
    t = None

    while (500, 0) not in s:
        i = 500
        for j in range(y+2):
            for d in [0, -1, 1]:
                if (i+d, j+1) not in s:
                    i += d
                    break
            else:
                break
        else:
            t = t or len(s) - n
        s.add((i,j))
    return (t, len(s) - n)
            
            

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
