from collections import defaultdict
import re

def get_data():
    with open("day16.txt") as f:
        text = f.read().strip()
    items = re.split(r"\n{2,}", text)
    # get rules
    lines = items[0].split("\n")
    rules = {}
    for line in lines:
        m = re.match(r"(.+?): (\d+)-(\d+) or (\d+)-(\d+)", line)
        field = m.group(1)
        end = len(m.groups())
        nums = [int(n) for n in m.groups()[1:]]
        rules[field] = nums
    # get my ticket
    line = items[1].split("\n")[1]
    my_ticket = [int(n) for n in line.split(",")]
    # get other tickets
    lines = items[2].split("\n")
    tickets = [[int(n) for n in line.split(",")] for line in lines[1:]]
    return rules, my_ticket, tickets


def set_from_range(nums):
    s1, e1, s2, e2 = nums
    return set(range(s1, e1 + 1)) | set(range(s2, e2 + 1))


def get_valid_nums(rules):
    valid_nums = set()
    for nums in rules.values():
        vn = set_from_range(nums)
        valid_nums.update(vn)
    return valid_nums


def part1():
    rules, my_ticket, tickets = get_data()
    all_valid_nums = get_valid_nums(rules)
    # check other tickets
    error_rate = 0
    for ticket in tickets:
        for num in ticket:
            if num not in all_valid_nums:
                error_rate += num
    return error_rate


def get_valid_nums_rules(rules):
    new_rules = {}
    for field, nums in rules.items():
        vn = set_from_range(nums)
        new_rules[field] = vn
    return new_rules


def get_next_field(possible):
    pos = None
    field = None
    for field, positions in possible.items():
        # find the field with only one possible position
        if len(positions) == 1:
            return field, positions[0]
    raise Exception("No valid field found")


def part2():
    rules, my_ticket, tickets = get_data()
    valid_nums = get_valid_nums(rules)
    # only keep valid tickets
    tickets.append(my_ticket)
    tickets = [t for t in tickets if all(n in valid_nums for n in t)]
    # get valid numbers for each rule
    rules = get_valid_nums_rules(rules)
    # get possible positions for each field
    possible = defaultdict(list)
    for field, nums in rules.items():
        for i in range(len(my_ticket)):
            valid = True
            for ticket in tickets:
                if ticket[i] not in nums:
                    valid = False
                    break
            if valid is True:
                possible[field].append(i)
    # determine positions for each field
    field_positions = {}
    while len(possible) > 0:
        field, pos = get_next_field(possible)
        field_positions[field] = pos
        # remove field and position from remaining
        possible.pop(field)
        for positions in possible.values():
            positions.remove(pos)
    # multiply "departure" fields
    product = 1
    for field, pos in field_positions.items():
        if "departure" in field:
            product *= my_ticket[pos]
    return product


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
    print(f"Part 2:\n{part2()}")
