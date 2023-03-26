def sums(inp):
    return [sum(map(int, i.split("\n"))) for i in inp.strip().split("\n\n")]

def solve1(inp):
    return max(sums(inp))

def solve2(inp):
    return sum(sorted(sums(inp))[-3:])

################################################################################
import pyperclip

main = solve2

test_input = r"""
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

print(str(main(test_input)))

input_fname = "/home/will/Documents/personal/aoc2022/1/input"
with open(input_fname) as f:
    pyperclip.copy(str(main(f.read())))
