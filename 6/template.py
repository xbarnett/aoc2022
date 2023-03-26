import itertools as i
import math as m
import re as r
from utils import *

def solve1(inp):
    inp = inp.strip().split("\n")
    inp = inp[0]
    for i in range(len(inp)-13):
        if len(set(inp[i:i+14])) == 14:
            return i+14
            

def solve2(inp):
    inp = inp.strip().split("\n")
    return inp

################################################################################
import pyperclip

main = solve1

test_input = r"""
mjqjpqmgbljsphdztnvjfqwrcgsmlb
"""

print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    pyperclip.copy(str(main(f.read())))
