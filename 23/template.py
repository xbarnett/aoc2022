from itertools import *
from math import *
from re import *
from utils import *
#from networkx import *

# findall(r"\d+", s)

def pri(z):
    mx = 100000
    Mx = -100000
    my = 1000000
    My = -1000000
    for ((x,y),elf) in z.items():
        if elf == ".":
            continue
        mx=min(mx,x)
        Mx=max(Mx,x)
        my=min(my,y)
        My=max(My,y)
    r = ""
    for i in range(mx,Mx+1):
        l = ""
        for j in range(my,My+1):
            l += z.get((i,j),".")
        r += l+"\n"
    print(r)

def solve1(inp):
    inp = inp.strip().split("\n")
    z = {}
    for (r,row) in enumerate(inp):
        for (c,tile) in enumerate(row):
            z[(r+1,c+1)] = tile
    dirs = "nswe"
    i = 0
    while True:
        reqs = {}
        #pri(z)
        for ((x,y),elf) in z.copy().items():
            if elf == ".":
                continue
            pos = set()
            for px in range(x-1,x+2):
                for py in range(y-1,y+2):
                    if px == x and py == y:
                        continue
                    elif z.get((px,py),".") != ".":
                        pos.add((px-x,py-y))
            if len(pos) == 0:
                continue
            for d in dirs[i%4:]+dirs[:i%4]:
                if d == "n" and all(p[0] != -1 for p in pos):
                    reqs[(x-1,y)] = reqs.get((x-1,y),[]) + [(x,y)]
                    break
                if d == "s" and all(p[0] != 1 for p in pos):
                    reqs[(x+1,y)] = reqs.get((x+1,y),[]) + [(x,y)]     
                    break
                if d == "e" and all(p[1] != 1 for p in pos):
                    reqs[(x,y+1)] = reqs.get((x,y+1),[]) + [(x,y)]
                    break
                if d == "w" and all(p[1] != -1 for p in pos):
                    reqs[(x,y-1)] = reqs.get((x,y-1),[]) + [(x,y)]
                    break
        nomove = True
        for t,f in reqs.items():
            if len(f) != 1:
                continue
            z[f[0]] = "."
            z[t] = "#"
            nomove = False
        if nomove:
            break
        i += 1
    return i+1

    # part 1 stuff
    mx = 100000
    Mx = -100000
    my = 1000000
    My = -1000000
    for ((x,y),elf) in z.items():
        if elf == ".":
            continue
        mx=min(mx,x)
        Mx=max(Mx,x)
        my=min(my,y)
        My=max(My,y)
    r = 0
    for i in range(mx,Mx+1):
        for j in range(my,My+1):
            if z.get((i,j),".") == ".":
                r += 1
    return r
            
                    
def solve2(inp):
    inp = inp.strip().split("\n")
    return inp

################################################################################
import pyperclip

main = solve1
test = True
real = True

test_input = r"""
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
"""

test_input2 = r"""
.....
..##.
..#..
.....
..##.
.....
"""

if test:
    print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if real:
        sol = main(f.read())
        print(sol)
        pyperclip.copy(str(sol))
