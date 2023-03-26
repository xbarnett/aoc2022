from itertools import *
from math import *
from re import *
from utils import *
from networkx import *

# findall(r"\d+", s)

def solve1(inp):
    inp = inp.strip().split("\n")
    return inp

def solve2(inp):
    inp = inp.strip().split("\n")
    return inp

################################################################################
import pyperclip

main = solve1
test = True
real = True

test_input = r"""

"""

if test:
    print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if real:
        sol = main(f.read())
        print(sol)
        pyperclip.copy(str(sol))
