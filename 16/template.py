from itertools import *
from math import *
from re import *
from utils import *
from networkx import *


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def solve1(inp):
    inp = inp.strip().split("\n")
    z = {}
    for line in inp:
        n = line[6:8]
        i = int(findall(r"\d+", line)[0])
        vs = line[line.find("tunnel")+7:]
        while not ord("A") <= ord(vs[0]) <= ord("Z"):
            vs=vs[1:]
        vz = []
        for v in vs.split(", "):
            vz.append(v)
        z[n] = (i,vz)    
    real = {}
    for i,(x,c) in z.items():
        if x > 0:
            real[i] = x
    vals = {}
    for ops in powerset(real):
        ops = tuple(sorted(ops))
        vals[ops] = sum(real[a] for a in ops)
    y = {}
    for n,(i,l) in z.items():
        for ops in vals:
            ops = tuple(sorted(ops))
            y[(n,ops,0)] = 0
            y[(n,ops,1)] = vals[ops]
    for j in range(2,30+1):
        print("round",j)
        for n,(i,l) in z.items():
            for ops in vals:
                w = 0
                for d in l:
                    w=max(w,y[(d,ops,j-1)]+vals[ops])
                if n in real and n not in ops:
                    for d in l:
                        w=max(w,y[(d,tuple(sorted(ops+(n,))),j-2)]+i+2*vals[ops])
                y[(n,ops,j)] = w
    print(y["AA",(),30])

##def solve2(inp):
##    inp = inp.strip().split("\n")
##    g = Graph()
##    z = {}
##    for line in inp:
##        n = line[6:8]
##        g.add_node(n)
##        i = int(findall(r"\d+", line)[0])
##        vs = line[line.find("tunnel")+7:]
##        while not ord("A") <= ord(vs[0]) <= ord("Z"):
##            vs=vs[1:]
##        vz = []
##        for v in vs.split(", "):
##            vz.append(v)
##            g.add_edge(n,v)
##        z[n] = (i,vz)
##    d = {}
##    real = {}
##    for i,(x,c) in z.items():
##        if x > 0:
##            real[i] = x
##    for i in real:
##        for j in real:
##            d[(i,j)] = shortest_path_length(g,i,j)
##    vals = {}
##    for ops in powerset(real):
##        ops = tuple(sorted(ops))
##        vals[ops] = sum(real[a] for a in ops)
##    y = {}
##    for n in real:
##        (i,l)=z[n]
##        for ops in vals:
##            ops = tuple(sorted(ops))
##            y[(n,ops,0)] = 0
##            y[(n,ops,1)] = vals[ops]
##    q = 30
##    for j in range(2,q+1):
##        print("round",j)
##        for n in real:
##            (i,l)=z[n]
##            for ops in vals:
##                w = 0
##                for m in real:
##                    v = y.get((m,ops,j-d[(n,m)]))
##                    if v is not None:
##                        w=max(w,v+vals[ops]*d[(n,m)])
##                if n in real and n not in ops:
##                    for m in real:
##                        v = y.get((m,tuple(sorted(ops+(n,))),j-1-d[(n,m)]))
##                        if v is not None:
##                            w=max(w,v+i*d[(n,m)]+vals[ops]*(1+d[(n,m)]))
##                y[(n,ops,j)] = w
##    r1 = single_source_shortest_path_length(g,"AA")
##    r2 = [(k,y[(k,(),q)]) for k in real]
##    rf = 0
##    for n in real:
##        rf=max(rf,y[(n,(),q-r1[n])])
##    print(rf)

def solve2(inp):
    inp = inp.strip().split("\n")
    z = {}
    for line in inp:
        n = line[6:8]
        i = int(findall(r"\d+", line)[0])
        vs = line[line.find("tunnel")+7:]
        while not ord("A") <= ord(vs[0]) <= ord("Z"):
            vs=vs[1:]
        vz = []
        for v in vs.split(", "):
            vz.append(v)
        z[n] = (i,vz)    
    real = {}
    for i,(x,c) in z.items():
        if x > 0:
            real[i] = x
    vals = {}
    for ops in powerset(real):
        ops = tuple(sorted(ops))
        vals[ops] = sum(real[a] for a in ops)
    y = {}
    for sp,(n,(i,l)) in enumerate(z.items()):
        print("init phase", sp)
        for m in z.keys():
            for ops in vals:
                ops = tuple(sorted(ops))
                y[(n,m,ops,0)] = 0
    
    for j in range(1,26+1):
        print("round",j)
        for sp,(n,(i,l)) in enumerate(z.items()):
            print("    subround",sp)
            for m,(i2,l2) in z.items():
                for ops in vals:
                    w = 0
                    for d in l:
                        for d2 in l2:
                            w=max(w,y[(d,d2,ops,j-1)]+vals[ops])
                        if m in real and m not in ops:
                            w=max(w,y[(d,m,tuple(sorted(ops+(m,))),j-1)]+vals[ops])
                    if n in real and n not in ops:
                        for d2 in l2:
                            w=max(w,y[(n,d2,tuple(sorted(ops+(n,))),j-1)]+vals[ops])
                        if m in real and m not in ops:
                            if n == m:
                                t = (n,)
                            else:
                                t =(n,m)
                            w=max(w,y[(n,m,tuple(sorted(ops+t)),j-1)]+vals[ops])
                    y[(n,m,ops,j)] = w
    return y["AA","AA",(),26]

################################################################################
import pyperclip

main = solve2
test = True
real = True

test_input = r"""
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""

if test:
    print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if real:
        sol = main(f.read())
        print(sol)
        pyperclip.copy(str(sol))
