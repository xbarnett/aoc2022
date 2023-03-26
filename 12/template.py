from itertools import *
from math import *
from re import *
from utils import *
from networkx import *

# findall(r"\d+", s)

def solve1(inp):
    inp = inp.strip().split("\n")
    n = len(inp)
    m = len(inp[0])

    g = DiGraph()
    for i in range(n):
        for j in range(m):
            g.add_node((i,j))
    s = None
    e = None
    a = []
    for i in range(n):
        for j in range(m):
            q = inp[i][j]
            if q == "S":
                s = (i,j)
                q = "a"
            elif q == "E":
                e = (i,j)
                q = "z"
            if q == "a":
                a.append((i,j))
            for d in [(0,-1),(0,1),(-1,0),(1,0)]:
                if not ((0 <= i+d[0] < n) and (0 <= j+d[1] < m)):
                    continue
                p = inp[i+d[0]][j+d[1]]
                if p == "S":
                    p = "a"
                elif p == "E":
                    p = "z"
                if ord(p) - ord(q) <= 1:
                    g.add_edge((i,j),(i+d[0],j+d[1]),value=1)
    ps = dict(single_target_shortest_path_length(g, e))
    r = 100000000000000000000000
    for p in a:
        if p in ps:
            r = min(r,ps[p])
    return r
    
    

def solve2(inp):
    inp = inp.strip().split("\n")
    return inp

################################################################################
import pyperclip

main = solve1
real = True

test_input = r"""
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if real:
        sol = main(f.read())
        print(sol)
        pyperclip.copy(str(sol))
