import itertools
from math import *
from re import *
from utils import *
from networkx import *

# findall(r"\d+", s)

##    mo = n // max(b[0])
##    mc = n // max(b[1])
##    mb = n // max(b[2])
##    mg = n // max(b[3])
##    s = {}
##    for i,(ro,rc,rb,rg) in enumerate(itertools.product(range(mo),range(mc),range(mb),range(mg))):
##        print("phase",i)
##        for (o,c,b,g) in itertools.product(range(n), repeat=4):
##            s[(ro,rc,rb,rg,o,c,b,g,0)] = 0
##    for j in range(1,2):
##        for i,(ro,rc,rb,rg) in enumerate(itertools.product(range(mo),range(mc),range(mb),range(mg))):
##            print("phase",i)
##            for (o,c,b,g) in itertools.product(range(n), repeat=4):
##                
##    return "done"

#n = 24

# b costs
# rs robots
# ms resources
# t time left
##def qual(b,rs,ms,t):
##    if t == 14:
##        print("stage")
##
##    if t == 0:
##        return ms[3]
##    result = 0
##    possibles = [None]
##    for i in range(4): # rob type
##        enough = True
##        for j in range(4): # rec type
##            if b[i][j] > ms[j]:
##                enough = False
##        if enough:
##            possibles.append(i)
##    if 3 in possibles:
##        i=3
##        nrs = rs[:i] + (rs[i]+1,) + rs[i+1:]
##        nms = tuple(ms[j] - b[i][j] + rs[j] for j in range(4))
##        return qual(b,nrs,nms,t-1)
##    else:
##        for i in possibles:
##            if i == None:
##                nrs = rs
##                nms = tuple(ms[j] + rs[j] for j in range(4))
##            else:
##                if i == 0 and rs[0] >= max(b[1][0],b[2][0],b[3][0]):
##                    continue
##                if i == 1 and rs[1] >= b[2][1]:
##                    continue
##                if i == 2 and rs[2] >= b[3][1]:
##                    continue
##                nrs = rs[:i] + (rs[i]+1,) + rs[i+1:]
##                nms = tuple(ms[j] - b[i][j] + rs[j] for j in range(4))
##            oresult=qual(b,nrs,nms,t-1)
##            if oresult >= result:
##                result = oresult
##    return result

# rs robots
# ms resources
def advance(x,mo,b,states):
    result = set()
    for (rs,ms) in states:
        used3 = False
        for i in range(4):
            afford = True
            for j in range(4):
                if b[i][j] > ms[j]:
                    afford = False
                    break
            if afford:
                if i == 0 and rs[0] >= mo:
                    continue
                if x > 27 and i != 3:
                    continue
                nrs = rs[:i] + (rs[i]+1,) + rs[i+1:]
                nms = tuple(ms[j] - b[i][j] + rs[j] for j in range(4))
                result.add((nrs,nms))
                if i == 3:
                    used3 = True
        if not used3:
            nms = tuple(ms[j] + rs[j] for j in range(4))
            result.add((rs,nms))
    return result

def solve1(inp):
    inp = inp.strip().split("\n")
    z = []
    for line in inp:
        a = []
        b = []
        for m in finditer(r"costs ", line):
            a.append(m.end())
        for m in finditer(r"\.", line):
            b.append(m.start())
        c = []
        for i in range(4):
            s = line[a[i]:b[i]]
            nc = [0]*4
            for o in s.split(" and "):
                n,t = o.split()
                n=int(n)
                if t == "ore":
                    nc[0] = n
                elif t == "clay":
                    nc[1] = n
                else:
                    nc[2] = n
            c.append(nc)
        z.append(c)
    result = 1
    for j,b in enumerate(z[:3]):
        print("ENTRY", j)

        mo = max(b[1][0],b[2][0],b[3][0])
        
        s = set([((1,0,0,0),(0,0,0,0))])
        i = 0
        while i < 32:
            s = advance(i,mo,b,s)
            i += 1
            print("phase",i,"length",len(s))
        r = max(i[1][3] for i in s)
        print()
        result *= r
    return result
    

def solve2(inp):
    inp = inp.strip().split("\n")
    return inp

################################################################################
import pyperclip

main = solve1
real = True

test_input = r"""
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
"""

#print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if real:
        sol = main(f.read())
        print(sol)
        pyperclip.copy(str(sol))
