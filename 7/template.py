from itertools import *
from math import *
from re import *
from utils import *

# findall(r"\d+", s)

def solve1(inp):
    inp = inp.strip().split("\n")
    dirs = {}
    cd = ()
    ldir = None
    for line in inp:
        if line[0] == "$":
            
            ldir = None
        if line[2:4] == "cd":
            if line[5:] == "..":
                cd = cd[:-1]
            elif line[5:] == "/":
                cd = ("/",)
            else:
                cd = cd + (line[5:],)
        elif line[2:4] == "ls":
            if line != "$ ls":
                ldir = cd + (line[5:],)
            else:
                ldir = cd
        elif ldir:
            (a, b) = line.split()
            if a == "dir":
                pass
            else:
                dirs[ldir + (b,)] = int(a)
    v = {}
    for (t, r) in dirs.items():
        for i in range(len(t)-1):
            d = t[1:1+i]
            v[d] = v.get(d,0) + r
    r = v[()]
    goal = 40000000
    ans = 1000000000000000
    for d in v:
        if r - v[d] <= goal:
            ans = min(ans, v[d])
    return ans

def solve2(inp):
    inp = inp.strip().split("\n")
    return inp

################################################################################
import pyperclip

main = solve1

test_input = r"""
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if True:
        pyperclip.copy(str(main(f.read())))
