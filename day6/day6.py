import re


def get_groups():
    with open("day6.txt") as f:
        text = f.read()
    return re.split(r"\n{2,}", text)


def part1():
    groups = get_groups()
    count = 0
    for group in groups:
        group = re.sub(r"\s+", "", group)
        count += len(set(group))
    return count


def part2():
    groups = get_groups()
    count = 0
    for group in groups:
        s = set(group)
        for person in group.split():
            s &= set(person.strip())
        count += len(s)
    return count


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
    print(f"Part 2:\n{part2()}")
