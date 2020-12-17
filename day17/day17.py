def get_data1():
    with open("day17.txt") as f:
        lines = [line.strip() for line in f]
    active = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                active.add((x, y, 0))
    return active


def get_neighbors1(pos):
    x, y, z = pos
    neighbors = set()
    for a in range(x - 1, x + 2):
        for b in range(y - 1, y + 2):
            for c in range(z - 1, z + 2):
                neighbors.add((a, b, c))
    neighbors.remove(pos)
    return neighbors


def part1():
    active = get_data1()
    for _ in range(6):
        new_active = set()
        unactive = set()
        # find positions that remain active
        for pos in active:
            neighbors = get_neighbors1(pos)
            count = 0
            for n in neighbors:
                if n in active:
                    count += 1
                else:
                    unactive.add(n)
            if count == 2 or count == 3:
                new_active.add(pos)
        # find positions that become active
        for pos in unactive:
            neighbors = get_neighbors1(pos)
            count = sum(1 for n in neighbors if n in active)
            if count == 3:
                new_active.add(pos)
        active = new_active
    return len(active)


def get_data2():
    with open("day17.txt") as f:
        lines = [line.strip() for line in f]
    active = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                active.add((x, y, 0, 0))
    return active


def get_neighbors2(pos):
    x, y, z, w = pos
    neighbors = set()
    for a in range(x - 1, x + 2):
        for b in range(y - 1, y + 2):
            for c in range(z - 1, z + 2):
                for d in range(w - 1, w + 2):
                    neighbors.add((a, b, c, d))
    neighbors.remove(pos)
    return neighbors


def part2():
    active = get_data2()
    for _ in range(6):
        new_active = set()
        unactive = set()
        # find positions that remain active
        for pos in active:
            neighbors = get_neighbors2(pos)
            count = 0
            for n in neighbors:
                if n in active:
                    count += 1
                else:
                    unactive.add(n)
            if count == 2 or count == 3:
                new_active.add(pos)
        # find positions that become active
        for pos in unactive:
            neighbors = get_neighbors2(pos)
            count = sum(1 for n in neighbors if n in active)
            if count == 3:
                new_active.add(pos)
        active = new_active
    return len(active)


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
    print(f"Part 2:\n{part2()}")
