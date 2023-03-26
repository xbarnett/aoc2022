import itertools as i
import math as m
import re as r
from utils import *

def solve1(inp):
    inp = inp.strip().split("\n")
    score = 0
    for line in inp:
        their, mine = line.split()
        their = ord(their) - ord("A")
        mine = ord(mine) - ord("X")
        if mine == 0:
            mine = (their+2)%3
        elif mine == 1:
            mine = their
        else:
            mine = (their+1)%3
        
        #mine = ord(mine) - ord("X")
        score += mine + 1
        if their == mine:
            score += 3
        elif (their+1)%3 == mine:
            score += 6
        else:
            score += 0
    return score


def solve2(inp):
    inp = inp.strip().split("\n")
    return inp

################################################################################
import pyperclip

main = solve1

test_input = r"""
A Y
B X
C Z
"""

print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    pyperclip.copy(str(main(f.read())))
