import re

ACC = "acc"
JMP = "jmp"
NOP = "nop"

def get_program():
    prog = []
    with open("day8.txt") as f:
        for line in f:
            inst, arg_str = line.strip().split(" ")
            arg = int(arg_str)
            prog.append((inst, arg))
    return prog


def check_program(prog):
    accum = 0
    ptr = 0
    visited = set()
    while True:
        if ptr == len(prog):
            return accum, True
        if ptr in visited:
            return accum, False
        visited.add(ptr)
        inst, arg = prog[ptr]
        if inst == ACC:
            accum += arg
            ptr += 1
        elif inst == JMP:
            ptr += arg
        elif inst == NOP:
            ptr += 1


def part1():
    prog = get_program()
    accum, _ = check_program(prog)
    return accum


def part2():
    prog = get_program()
    # try each change
    for i in range(len(prog)):
        inst, arg = prog[i]
        new_inst = None
        if inst == JMP:
            new_inst = NOP
        elif inst == NOP and arg != 0:
            new_inst = JMP
        if new_inst is not None:
            prog[i] = (new_inst, arg)
            accum, result = check_program(prog)
            if result is True:
                return accum
            prog[i] = (inst, arg)


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
    print(f"Part 2:\n{part2()}")
