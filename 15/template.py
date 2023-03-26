from itertools import *
from math import *
from re import *
from utils import *
from networkx import *

def b(temp_tuple, start_index = 0):
    temp_tuple.sort(key=lambda interval: interval[0])
    merged = [temp_tuple[0]]
    for current in temp_tuple:
        previous = merged[-1]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current)
    return merged

def solve1(inp):
    inp = inp.strip().split("\n")
    z = {}
    my = 2000000
    my = 2000000
    bs = set()
    for line in inp:
        sx,sy,bx,by=map(int,findall(r"-?\d+", line))
        if by == my:
            bs.add(bx)
        z[(sx,sy)]=abs(sx-bx)+abs(sy-by)
    print(z)
    pos= []
    for (sx,sy),d in z.items():
        left = d-abs(sy-my)
        if left >= 0:
            pos.append([sx-left,sx+left])
    r = 0
    print(pos)
    m = b(pos)
    print(m)
    sub=0
    for (x,y) in m:
        for bi in bs:
            if x <= bi <= y:
                sub += 1
        r += y-x+1
    return r-sub

def solve2(inp):
    inp = inp.strip().split("\n")
    z = {}
    z0 = None
    for line in inp:
        sx,sy,bx,by=map(int,findall(r"-?\d+", line))
        z[(sx,sy)]=abs(sx-bx)+abs(sy-by)
        if z0 is not None:
            z0 = (sx,sy)
    #print(z)
    s = set()
    for z0 in z:
        print(z0)
        n = z[z0]+1
        x,y=z0
        #print(n)
        for i in range(n):
            for (a,b) in [(x+i,y-n+i),(x+n-i,y+i),(x-i,y+n-i),(x-n+i,y+i)]:
                if 0 <= a <= 4000000 and 0 <= b <= 4000000:
                    s.add((a,b))
    print((14,11) in s)
    for p in s:
        good = p
        for q,d in z.items():
            y = abs(p[0]-q[0])+abs(p[1]-q[1])
            if y <= d:
                good = None
                break
        if good is not None:
            return good
        
    
    

################################################################################
import pyperclip

main = solve2
real = True

test_input = r"""
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""

#print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if real:
        sol = main(f.read())
        print(sol)
        pyperclip.copy(str(sol))
