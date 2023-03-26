from itertools import *
from math import *
from re import *
from utils import *
from networkx import *

# findall(r"\d+", s)

def c(a,b):
    if type(a)==int and type(b) == int:
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0
    elif type(a) == int:
        return c([a], b)
    elif type(b) == int:
        return c(a,[b])
    elif a == []:
        if b == []:
            return 0
        else:
            return -1
    elif b == []:
        return 1
    else:
        r = c(a[0],b[0])
        if r in [-1,1]:
            return r
        else:
            return c(a[1:],b[1:])

def solve1(inp):
    inp = inp.strip().split("\n")
    i = 0
    r = 0
    while 3*i < len(inp):
        a = eval(inp[3*i])
        b = eval(inp[3*i+1])
        if c(a,b) == -1:
            r += i + 1
        i += 1
    return r
                
def solve2(inp):
    inp = inp.strip().split("\n")
    i = 0
    l = []
    while 3*i < len(inp):
        l.append(eval(inp[3*i]))
        l.append(eval(inp[3*i+1]))
        i += 1
    l.extend([[[2]],[[6]]])
    l.sort(key=cmp_to_key(c))
    d1 = None
    d2 = None
    for i,x in enumerate(l):
        if x == [[2]]:
            d1 = i+1
        if x == [[6]]:
            d2 = i + 1
    return d1*d2


################################################################################
import pyperclip

main = solve2
real = True

test_input = r"""
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""

print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if real:
        sol = main(f.read())
        print(sol)
        pyperclip.copy(str(sol))
