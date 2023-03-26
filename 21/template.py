from itertools import *
from math import *
from re import *
from utils import *
from networkx import *
from polynomial import Polynomial
# findall(r"\d+", s)

def solve1(inp):
    inp = inp.strip().split("\n")
    z = {}
    for line in inp:
        m, o = line.split(": ")
        try:
            o = int(o)
        except:
            o = o.split()
        z[m] = o
    print(z)
    v = {}
    for n,x in z.items():
        if type(x)==int:
            v[n] = x
    while True:
        more = False
        for n,x in z.items():
            if n not in v and type(x) != int and x[0] in v and x[2] in v:
                if x[1] == "+":
                    v[n] = v[x[0]] + v[x[2]]
                    more = True
                if x[1] == "-":
                    v[n] = v[x[0]] - v[x[2]]
                    more = True
                if x[1] == "*":
                    v[n] = v[x[0]] * v[x[2]]
                    more = True
                if x[1] == "/":
                    v[n] = v[x[0]] // v[x[2]]
                    more = True
        if not more:
            break
    print(v["root"])

# ([],[])
# rational function
  

def solve2(inp):
    inp = inp.strip().split("\n")
    z = {}
    for line in inp:
        m, o = line.split(": ")
        try:
            o = int(o)
        except:
            o = o.split()
        z[m] = o
    z["root"] = [z["root"][0],"=",z["root"][2]]
    v = {}
    for n,x in z.items():
        if type(x)==int:
            v[n] = Polynomial(x),Polynomial(1)
    v["humn"] = Polynomial(1,0),Polynomial(1)
    while True:
        for n,x in z.items():
            if n not in v and type(x) != int and x[0] in v and x[2] in v:
                (a,b) = v[x[0]]
                (c,d) = v[x[2]]
                if x[1] == "+":
                    v[n] = a*d+b*c,b*d
                if x[1] == "-":
                    v[n] = a*d-b*c,b*d
                if x[1] == "*":
                    v[n] = a*c,b*d
                if x[1] == "/":
                    v[n] = a*d,b*c
                if x[1] == "=":
                    return ((b[0]*c[0]//d[0])-a[0])//a[1]

################################################################################
import pyperclip

main = solve2
real = True

test_input = r"""
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
"""

print(str(main(test_input)))
print()

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if real:
        sol = main(f.read())
        print(sol)
        pyperclip.copy(str(sol))
