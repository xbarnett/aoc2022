from itertools import *
from math import *
from re import *
from utils import *

# findall(r"\d+", s)

def solve1(inp):
    inp = inp.strip().split("\n")
    x = [list(map(int, i)) for i in inp]
    good = 0
    n = len(x)
    for i in range(n):
        for j in range(n):
            a, b, c, d = True, True, True, True
            for k in range(i):
                if x[k][j] >= x[i][j]:
                    a = False
            for k in range(n-i-1):
                if x[n-1-k][j] >= x[i][j]:
                    b = False
            for k in range(j):
                if x[i][k] >= x[i][j]:
                    c = False
            for k in range(n-j-1):
                if x[i][n-1-k] >= x[i][j]:
                    d = False
            if a or b or c or d:
                good += 1
    return good
def solve2(inp):
    inp = inp.strip().split("\n")
    x = [list(map(int, i)) for i in inp]
    good = 0
    n = len(x)
    for i in range(n):
        for j in range(n):
            a, b, c, d = 0, 0, 0, 0
            for k in range(i):
                a += 1
                if x[i-1-k][j] >= x[i][j]:
                    break
            for k in range(n-i-1):
                b += 1
                if x[i+1+k][j] >= x[i][j]:
                    break
            for k in range(j):
                c += 1
                if x[i][j-1-k] >= x[i][j]:
                    break
            for k in range(n-j-1):
                d += 1
                if x[i][j+1+k] >= x[i][j]:
                    break
            r = a*b*c*d
            good=max(good, r)
    return good

################################################################################
import pyperclip

main = solve2
real = True

test_input = r"""
30373
25512
65332
33549
35390
"""

print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if real:
        pyperclip.copy(str(main(f.read())))
