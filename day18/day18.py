import re

def parse(tokens, i):
    units = []
    while i < len(tokens):
        t = tokens[i]
        i += 1
        if t == "(":
            sub_units, i = parse(tokens, i)
            units.append(sub_units)
        elif t == ")":
            return units, i
        else:
            if t.isdigit():
                t = int(t)
            units.append(t)
    return units, i


def get_data():
    with open("day18.txt") as f:
        lines = [line.strip() for line in f]
    hw_probs = []
    for line in lines:
        tokens = re.findall(r"\d+|\+|\*|\(|\)", line)
        units, _ = parse(tokens, 0)
        hw_probs.append(units)
    return hw_probs


def get_val1(item):
    if isinstance(item, int):
        return item
    if isinstance(item, list):
        return evaluate1(item)
    raise Exception("Expected int or list")


def evaluate1(exp):
    # get first value in expression
    val = get_val1(exp[0])
    # add or multiply remaining values
    for i in range(1, len(exp), 2):
        op = exp[i]
        v = get_val1(exp[i + 1])
        if op == "+":
            val += v
        elif op == "*":
            val *= v
        else:
            raise Exception("Expected + or *")
    return val


def part1():
    hw_probs = get_data()
    return sum(evaluate1(exp) for exp in hw_probs)


def get_val2(item):
    if isinstance(item, int):
        return item
    if isinstance(item, list):
        return evaluate2(item)
    raise Exception("Expected int or list")


def apply_operator(exp, op):
    while op in exp:
        # get values on either side of operator
        i = exp.index(op)
        val1 = get_val2(exp[i - 1])
        val2 = get_val2(exp[i + 1])
        # combine values into one
        val = None
        if op == "+":
            val = val1 + val2
        elif op == "*":
            val = val1 * val2
        else:
            raise Exception("Expected + or *")
        # replace pair of values with single value
        exp.pop(i + 1)
        exp.pop(i)
        exp[i - 1] = val


def evaluate2(exp):
    apply_operator(exp, "+")
    apply_operator(exp, "*")
    return int(exp[0])


def part2():
    hw_probs = get_data()
    return sum(evaluate2(exp) for exp in hw_probs)


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
    print(f"Part 2:\n{part2()}")
