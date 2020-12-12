import re

TARGET_BAG = "shiny gold bag"
NO_BAGS = "no other bags"

def get_bag_dict():
    bag_dict = {}
    with open("day7.txt") as f:
        for line in f:
            if NO_BAGS in line:
                continue
            parent_bag = re.match(r"^.+?bag", line).group(0)
            matches = re.findall(r"(\d+)\s+(.+?bag)", line)
            child_bags = [(m[1], int(m[0])) for m in matches]
            bag_dict[parent_bag] = child_bags
    return bag_dict


def check_bag(bag_dict, bag_color):
    stack = [bag_color]
    while len(stack) > 0:
        parent_bag = stack.pop(0)
        if parent_bag in bag_dict:
            child_bags = bag_dict[parent_bag]
            child_colors = [b[0] for b in child_bags]
            if TARGET_BAG in child_colors:
                return True
            stack += child_colors
    return False


def part1():
    bag_dict = get_bag_dict()
    count = 0
    for bag_color in bag_dict:
        if check_bag(bag_dict, bag_color):
            count += 1
    return count


def recurse(bag_dict, bag_name, mult):
    if bag_name not in bag_dict:
        return 0
    child_bags = bag_dict[bag_name]
    total = 0
    for child_bag, count in child_bags:
        total += count * mult
        total += recurse(bag_dict, child_bag, count * mult)
    return total


def part2():
    bag_dict = get_bag_dict()
    total = recurse(bag_dict, TARGET_BAG, 1)
    return total


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
    print(f"Part 2:\n{part2()}")
