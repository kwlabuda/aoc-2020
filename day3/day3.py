def count_trees(right, down):
    with open("day3.txt") as f:
        lines = [line.rstrip() for line in f]
    trees = 0
    x = 0
    y = 0
    while y < len(lines):
        line = lines[y]
        idx = x % len(line)
        if line[idx] == "#":
            trees += 1
        x += right
        y += down
    return trees


def part1():
    return count_trees(3, 1)


def part2():
    product = 1
    product *= count_trees(1, 1)
    product *= count_trees(3, 1)
    product *= count_trees(5, 1)
    product *= count_trees(7, 1)
    product *= count_trees(1, 2)
    return product


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
    print(f"Part 2:\n{part2()}")
