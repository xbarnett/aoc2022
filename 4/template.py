import itertools as i
import math as m
import re as r
from utils import *

def solve1(inp):
    inp = inp.strip().split("\n")
    ans = 0
    for line in inp:
        n = line.split(",")
        m = []
        for s in n:
            for r in s.split("-"):
                m.append(int(r))
        if m[2] <= m[1] and m[3] >= m[0]:
            ans += 1
    return ans
        
def solve2(inp):
    inp = inp.strip().split("\n")
    return inp

################################################################################
import pyperclip

main = solve1
real = True

test_input = r"""
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if real:
        pyperclip.copy(str(main(f.read())))
