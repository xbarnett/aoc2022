from itertools import *
from math import *
from re import *
from utils import *
from networkx import *

# findall(r"\d+", s)

def ston(s):
    r = 0
    for c in s:
        r *= 5
        if "0" <= c <= "2":
            r += ord(c) - ord("0")
        elif c == "-":
            r -= 1
        else:
            r -= 2
    return r

def ntos(n):
    s = ""
    if n == 0:
        s = "0"
    else:
        while n != 0:
            s += str(n%5)
            n //= 5
    s = s[::-1]
    ns = ""
    for c in s:
        if "0" <= c <= "2":
            ns += c
        elif c == "3":
            ns = ntos(ston(ns)+1)+"="
        else:
            ns = ntos(ston(ns)+1)+"-"
    return ns

def solve1(inp):
    inp = inp.strip().split("\n")
    r = 0
    for s in inp:
        r += ston(s)
    return ntos(r)

def solve2(inp):
    inp = inp.strip().split("\n")
    return inp

################################################################################
import pyperclip

main = solve1
test = True
real = True

test_input = r"""
1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122

"""

if test:
    print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if real:
        sol = main(f.read())
        print(sol)
        pyperclip.copy(str(sol))
