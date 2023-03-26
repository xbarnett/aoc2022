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

    items = {}
    for i in range(10000):
        print(i)
        for j, m in enumerate(ms):
            for w in m[0]:
                items[j] = items.get(j, 0) + 1
                w = calc(m[1], w)
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
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""

print(str(main(test_input)))

input_fname = "/home/will/Downloads/input"
with open(input_fname) as f:
    if real:
      pyperclip.copy(str(main(f.read())))

