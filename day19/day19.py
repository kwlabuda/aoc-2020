from collections import defaultdict
import re

def get_data(path):
    with open(path) as f:
        text = f.read()
    rule_str, message_str = re.split(r"\n{2,}", text)
    rules = {}
    rule_lines = rule_str.strip().split("\n")
    for line in rule_lines:
        tokens = line.split()
        t = tokens[0].rstrip(":")
        rule_num = int(t)
        if "|" in line:
            i = tokens.index("|")
            run1 = tuple(int(t) for t in tokens[1:i])
            run2 = tuple(int(t) for t in tokens[i + 1:])
            rules[rule_num] = [run1, run2]
        elif "\"" in line:
            # single character
            rules[rule_num] = [tokens[1].strip("\"")]
        else:
            # list of rules
            run = tuple(int(t) for t in tokens[1:])
            rules[rule_num] = [run]
    messages = message_str.strip().split("\n")
    return rules, messages


def get_cnf(rules):
    # https://en.wikipedia.org/wiki/Chomsky_normal_form
    # https://web.stanford.edu/~jurafsky/slp3/13.pdf page 4

    # copy all conforming rules to the new grammar
    cnf_rules = defaultdict(list)
    remaining = defaultdict(list)
    for left, rights in rules.items():
        for right in rights:
            if isinstance(right, str):
                cnf_rules[left].append(right)
            else:
                remaining[left].append(right)

    # convert unit productions
    remaining2 = defaultdict(list)
    for left, rights in remaining.items():
        for right in rights:
            while len(right) == 1 and isinstance(right[0], int):
                right = rules[right[0]]
            if len(right) == 1:
                cnf_rules[left].append(right[0])
            elif isinstance(right, list):
                remaining2[left] += right
            elif isinstance(right, tuple):
                remaining2[left].append(right)

    # make all rules binary and add them to new grammar
    rule_idx = max(rules) + 1
    for left, rights, in remaining2.items():
        for right in rights:
            if len(right) == 2:
                cnf_rules[left].append(tuple(right))
            else:
                cnf_rules[left].append((right[0], rule_idx))
                for i in range(1, len(right) - 2):
                    cnf_rules[rule_idx] = [right[i], rule_idx + 1]
                    rule_idx += 1
                cnf_rules[rule_idx].append((right[-2], right[-1]))
                rule_idx += 1
    return cnf_rules


def check_message(cnf_rules, msg):
    # https://en.wikipedia.org/wiki/CYK_algorithm
    P = set()
    msg_len = len(msg)
    # find all s, v such that the char
    # at s can be generated from rule v
    for s in range(1, len(msg) + 1):
        char = msg[s - 1]
        for left, rights in cnf_rules.items():
            for right in rights:
                if isinstance(right, str) and right == char:
                    P.add((1, s, left))
    # find all l, s, v such that the substring
    # of length l at s can be generated from rule v
    for l in range(2, msg_len + 1):
        for s in range(1, msg_len - l + 2):
            for p in range(1, l):
                for left, rights in cnf_rules.items():
                    for right in rights:
                        if not isinstance(right, tuple):
                            continue
                        b, c = right
                        if (p, s, b) in P and (l - p, s + p, c) in P:
                            P.add((l, s, left))
    return (msg_len, 1, 0) in P


def part1():
    rules, messages = get_data("day19.txt")
    cnf_rules = get_cnf(rules)
    return sum(1 for msg in messages if check_message(cnf_rules, msg))


def part2():
    rules, messages = get_data("day19.txt")
    rules[8].append((42, 8))
    rules[11].append((42, 11, 31))
    cnf_rules = get_cnf(rules)
    return sum(1 for msg in messages if check_message(cnf_rules, msg))


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
    print(f"Part 2:\n{part2()}")
