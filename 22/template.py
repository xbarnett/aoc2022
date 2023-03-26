from itertools import *
from math import *
from re import *
from utils import *
from networkx import *

# findall(r"\d+", s)

def solve1(inp):
    inp = inp.split("\n")[:-1]
    print(inp)
    m = {}
    p = None
    for (i,line) in enumerate(inp):
        if line == "":
            break
        for (j,tile) in enumerate(line):
            if tile != " ":
                if p is None:
                    p = (i+1,j+1)
                m[(i+1,j+1)] = tile
    rows = {}
    cols = {}
    for (r,c) in m:
        if (r,c) == (1,1):
            print("hi")
        rows[r] = [min(c,rows.get(r, [10000,-10000])[0]),
                   max(c,rows.get(r, [10000,-10000])[1])]
        cols[c] = [min(r,cols.get(c, [10000,-10000])[0]),
                   max(r,cols.get(c, [10000,-10000])[1])]
    ins = " "+inp[-1]
    lets = [0]
    for (i,c) in enumerate(ins):
        if "A" <= c <= "Z":
            lets.append(i)
    lets.append(len(ins))
    jns = []
    for i in range(len(lets)-1):
        jns.append(ins[lets[i]:lets[i+1]])
    f = (0,1)
    for j in jns:
        a = j[0]
        j = int(j[1:])
        if a == "R":
            f = {(0,1): (1,0), (1,0): (0,-1), (0,-1): (-1,0), (-1,0): (0,1)}[f]
        elif a == "L":
            f = {(1,0): (0,1), (0,-1): (1,0), (-1,0): (0,-1), (0,1): (-1,0)}[f]
        for _ in range(j):
            h,H = rows[p[0]]
            v,V = cols[p[1]]
            np = ((p[0]+f[0]-v)%(V-v+1)+v,(p[1]+f[1]-h)%(H-h+1)+h)
            if m[np] != "#":
                p = np
    return 1000*p[0]+4*p[1]+{(0,1):0,(1,0):1,(0,-1):2,(-1,0):3}[f]

def solve2(inp):
    inp = inp.split("\n")[:-1]
    m = {}
    p = None
    for (i,line) in enumerate(inp):
        if line == "":
            break
        for (j,tile) in enumerate(line):
            if tile != " ":
                if p is None:
                    p = (i+1,j+1)
                m[(i+1,j+1)] = tile
    ins = " "+inp[-1]
    lets = [0]
    for (i,c) in enumerate(ins):
        if "A" <= c <= "Z":
            lets.append(i)
    lets.append(len(ins))
    jns = []
    for i in range(len(lets)-1):
        jns.append(ins[lets[i]:lets[i+1]])
    f = (0,1)
    for j in jns:
        a = j[0]
        j = int(j[1:])
        if a == "R":
            f = {(0,1): (1,0), (1,0): (0,-1), (0,-1): (-1,0), (-1,0): (0,1)}[f]
        elif a == "L":
            f = {(1,0): (0,1), (0,-1): (1,0), (-1,0): (0,-1), (0,1): (-1,0)}[f]
        for _ in range(j):
            r,c=(p[0]-1)//50,(p[1]-1)//50
            #r,c=(p[0]-1)//4,(p[1]-1)//4
            face = {(0,1):1, (0,2):2, (1,1):3, (2,0):4, (2,1):5, (3,0): 6}[(r,c)]
            #face = {(0,2):1, (1,0):2, (1,1):3, (1,2):4, (2,2):5, (2,3): 6}[(r,c)]
            bounds = {1:(1,51), 2:(1,101), 3:(51,51), 4:(101,1), 5:(101,51), 6:(151,1)}
            #bounds = {1:(1,9), 2:(5,1), 3:(5,5), 4:(5,9), 5:(9,9), 6:(9,13)}
            
            np = p[0]+f[0],p[1]+f[1]
            right = (0,1)
            left = (0,-1)
            up = (-1,0)
            down = (1,0)
            twist = {(1,left):(4,right),(1,right):(2,right),(1,down):(3,down),(1,up):(6,right),
                     (2,left):(1,left),(2,right):(5,left),(2,down):(3,left),(2,up):(6,up),
                     (3,left):(4,down),(3,right):(2,up),(3,down):(5,down),(3,up):(1,up),
                     (4,left):(1,right),(4,right):(5,right),(4,down):(6,down),(4,up):(3,right),
                     (5,left):(4,left),(5,right):(2,left),(5,up):(3,up),(5,down):(6,left),
                     (6,left):(1,down),(6,right):(5,up),(6,down):(2,down),(6,up):(4,up)}
##            twist = {(1,left):(3,down),(1,right):(6,left),(1,down):(4,down),(1,up):(2,down),
##                     (2,left):(6,up),(2,right):(3,right),(2,down):(5,up),(2,up):(1,down),
##                     (3,left):(2,left),(3,right):(4,right),(3,down):(5,right),(3,up):(1,right),
##                     (4,left):(3,left),(4,right):(6,down),(4,down):(5,down),(4,up):(1,up),
##                     (5,left):(3,up),(5,right):(6,right),(5,up):(4,up),(5,down):(2,up),
##                     (6,left):(5,left),(6,right):(1,left),(6,down):(2,right),(6,up):(4,left)}
            #y = 4
            y = 50
            if np[1] < bounds[face][1]:
                (nface,nf) = twist[(face,left)]
                flip = {left:"v",right:"h",down:"d1",up:"d2"}[nf]
            elif np[1] >= bounds[face][1] + y:
                (nface,nf) = twist[(face,right)]
                flip = {left:"h",right:"v",down:"d2",up:"d1"}[nf]
            elif np[0] < bounds[face][0]:
                (nface,nf) = twist[(face,up)]
                flip = {left:"d2",right:"d1",down:"v",up:"h"}[nf]
            elif np[0] >= bounds[face][0] + y:
                (nface,nf) = twist[(face,down)]
                flip = {left:"d1",right:"d2",down:"h",up:"v"}[nf]
            else:
                (nface,nf) = face,f
                flip = "n"
            sp = p[0]-bounds[face][0],p[1]-bounds[face][1]
            if flip == "v":
                sp = (sp[0],y-1-sp[1])
            elif flip == "h":
                sp = (y-1-sp[0],sp[1])
            elif flip == "d1":
                sp = (sp[1],sp[0])
            elif flip == "d2":
                sp = (y-1-sp[1],y-1-sp[0])
            if flip != "n":
                np = (bounds[nface][0]+sp[0], bounds[nface][1]+sp[1])
            if m[np] != "#":
                p = np
                f = nf
    return 1000*p[0]+4*p[1]+{(0,1):0,(1,0):1,(0,-1):2,(-1,0):3}[f]

################################################################################
import pyperclip

main = solve2
real = True

test_input = r"""        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
"""

#print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if real:
        sol = main(f.read())
        print(sol)
        pyperclip.copy(str(sol))
