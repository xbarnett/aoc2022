from itertools import *
from math import *
from re import *
from utils import *

# findall(r"\d+", s)

def calc(rule, n):
    _, _, rule = rule.partition("= ")
    return eval(rule, {"old":n})

def solve1(inp):
    inp = inp.strip().split("\n")
    rules = [i[13:] for i in inp[2::7]]
    items = [list(map(int,findall(r"\d+", i))) for i in inp[1::7]]
    tests = [list(map(int,findall(r"\d+", i)))[0] for i in inp[3::7]]
    tms = [list(map(int,findall(r"\d+", i)))[0] for i in inp[4::7]]
    fms = [list(map(int,findall(r"\d+", i)))[0] for i in inp[5::7]]

    ms = [[items[i], rules[i], tests[i], tms[i], fms[i]] for i in range(len(rules))]

    trick = 1
    for i in tests:
        trick *= i
    items = {}
    for i in range(10000):
        for j, m in enumerate(ms):
            for w in m[0]:
                items[j] = items.get(j, 0) + 1
                w = calc(m[1], w) % trick
                #w //= 3
                if w % m[2] == 0:
                    ms[m[3]][0].append(w)
                else:
                    ms[m[4]][0].append(w)
            m[0] = []
    print(items)
    r = list(items.values())
    r.sort()
    return r[-1]*r[-2]
   

def solve2(inp):
    inp = inp.strip().split("\n")
    return inp

###################################['test']#############################################
import pyperclip

main = solve1
real = True

test_input = r"""
Monkey 0:
  Starting items: 69, 69
  Operation: new = print("LMAO"); return 69
  Test: divisible by 420
    If true: throw to monkey 1
    If false: throw to monkey 1

Monkey 1:
  Starting items: 69, 69
  Operation: new = print("LMAO"); return 69
  Test: divisible by 420
    If true: throw to monkey 0
    If false: throw to monkey 0
"""

print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if real:
      pyperclip.copy(str(main(f.read())))
