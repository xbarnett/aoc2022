import itertools as i
import math as m
import re as r
from utils import *

def solve1(inp):
    #inp = inp.strip().split("\n")
    inp = " "+inp[1:-1]
    lets = []
    m = 0
    for line in inp.split("\n\n")[0].split("\n")[:-1]:
        m = max(len(line)//4, m)
    m += 1
    print(m)
    for line in inp.split("\n\n")[0].split("\n")[:-1]:
        row = []
        print(line)
        for i in range(m):
            try:
                row.append(line[4*i+1])
            except:
                row.append(' ')
        lets.append(row)
    print(lets)
    lets = [[lets[j][i] for j in range(len(lets))] for i in range(len(lets[0]))]
    x = []
    for l in lets:
        x.append(list("".join(l).strip())[::-1])
    for line in inp.split("\n\n")[1].split("\n"):
        i = line.find(" from")
        a = line[5:i]
        b = line[i + 6]
        c = line[i + 11]
        a,b,c=int(a),int(b),int(c)
        l = x[b-1][-a:]
        x[b-1] = x[b-1][:-a]
        x[c-1].extend(l)
    r = ""
    print(x)
    return "".join([i[-1] for i in x])
    

def solve2(inp):
    inp = inp.strip().split("\n")
    return inp

################################################################################
import pyperclip

main = solve1
real = True

test_input = r"""
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

#print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if real:
        pyperclip.copy(str(main(f.read())))
