from itertools import *
from math import *
from re import *
from utils import *
from networkx import *

# findall(r"\d+", s)

def solve1(inp):
    inp = inp.strip().split("\n")
    z = set()
    mx = 1000
    Mx = -1000
    my = 1000
    My = -1000
    mz = 1000
    Mz = -100
    for line in inp:
        z.add(tuple(map(int,line.split(","))))
    for (a,b,c) in z:
        mx=min(mx,a)
        Mx=max(Mx,a)
        my=min(my,b)
        My=max(My,b)        
        mz=min(mz,c)
        Mz=max(Mz,c)
    print(mx,Mx,my,My,mz,Mz)
    out = set([(mx-1,my-1,mz-1)])
    while True:
        new = set()
        for (a,b,c) in out:
            for p in [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]:
                p2 = (a+p[0],b+p[1],c+p[2])
                if p2 not in out and mx-1 <= p2[0] <= Mx+1 and my-1 <= p2[1] <= My+1 and mz-1 <= p2[2] <= Mz+1:
                    if p2 not in z:
                        new.add(p2)
        for p in new:
            out.add(p)
        if new == set():
            break
    ans = 0
    for (a,b,c) in z:
        for p in [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]:
            p2 = (a+p[0],b+p[1],c+p[2])
            if p2 not in z and p2 in out:
                ans += 1
    return ans

def solve2(inp):
    inp = inp.strip().split("\n")
    return inp

################################################################################
import pyperclip

main = solve1
real = True

test_input = r"""
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""

print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if real:
        sol = main(f.read())
        print(sol)
        pyperclip.copy(str(sol))
