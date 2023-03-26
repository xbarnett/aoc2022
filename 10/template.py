from itertools import *
from math import *
from re import *
from utils import *

# findall(r"\d+", s)

def solve1(inp):
    inp = inp.strip().split("\n")
    x = 1
    ip = 0
    c = 1
    half = False
    r = 0
    r2 = {}
    sx, sy = (c-1)%40, ((c-1)%240)//40
    if abs(x-sx) <= 1:
        r2[(sx,sy)] = "#"
    else:
        r2[(sx,sy)] = "."
    while ip < len(inp):
        if inp[ip] == "noop":
            c += 1
            ip += 1
        else:
            i, y = inp[ip].split()
            y=int(y)
            if half:
                c += 1
                ip += 1
                half = False
                x += y
            else:
                c += 1
                half = True
        if c in [20, 60, 100, 140, 180, 220]:
            print(c,x)
            r += c * x
        sx, sy = (c-1)%40, ((c-1)%240)//40
        if abs(x-sx) <= 1:
            r2[(sx,sy)] = "#"
        else:
            r2[(sx,sy)] = "."
    for i in range(6):
        s = "".join([r2.get((k, i), ".") for k in range(40)])
        print(s)

def solve2(inp):
    inp = inp.strip().split("\n")
    return inp

################################################################################
import pyperclip

main = solve1
real = True

test_input = r"""
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if real:
      pyperclip.copy(str(main(f.read())))
