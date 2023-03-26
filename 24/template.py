from itertools import *
from math import *
from re import *
from utils import *
from networkx import *

# findall(r"\d+", s)

def solve1(inp):
    inp = inp.strip().split("\n")
    bliz = {}
    for (r,row) in enumerate(inp[1:-1]):
        for (c,tile) in enumerate(row[1:-1]):
            if tile != ".":
                bliz[(r,c)] = [tile]
            else:
                bliz[(r,c)] = []
    rows = len(inp[1:-1])
    cols = len(inp[0][1:-1])
    reach = set([(-1,0)])
    bliz[(-1,0)] = []
    bliz[(rows,cols-1)] = []
    time = 0
    for phase in range(3):
        while True:
            #print(reach)
            if phase == 0 and (rows,cols-1) in reach:
                reach = set([(rows,cols-1)])
                break
            if phase == 1 and (-1,0) in reach:
                reach = set([(-1,0)])
                break
            if phase == 2 and (rows,cols-1) in reach:
                return time
            nb = {}
            for ((r,c),tiles) in bliz.items():
                for tile in tiles:
                    if tile == ">":
                        nb[(r,(c+1)%cols)] = nb.get((r,(c+1)%cols),[])+ [tile]
                    elif tile == "<":
                        nb[(r,(c-1)%cols)] = nb.get((r,(c-1)%cols),[]) + [tile]
                    elif tile == "^":
                        nb[((r-1)%rows,c)] = nb.get(((r-1)%rows,c),[]) + [tile]
                    elif tile == "v":
                        nb[((r+1)%rows,c)] = nb.get(((r+1)%rows,c),[]) + [tile]
            bliz = nb
            bliz[(-1,0)] = []
            bliz[(rows,cols-1)] = []
            nr = set()
            for (r,c) in reach:
                for dx in range(-1,2):
                    for dy in range(-1,2):
                        if dx != 0 and dy != 0:
                            continue
                        if (0 <= r+dx < rows and 0 <= c+dy < cols) or (r+dx,c+dy)==(rows,cols-1) or (r+dx,c+dy)==(-1,0):
                            if bliz.get((r+dx,c+dy),[]) == []:
                                nr.add((r+dx,c+dy))
            reach = nr
            time += 1                   

        

def solve2(inp):
    inp = inp.strip().split("\n")
    return inp

################################################################################
import pyperclip

main = solve1
test = True
real = True

test_input = r"""
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
"""

if test:
    print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if real:
        sol = main(f.read())
        print(sol)
        pyperclip.copy(str(sol))
