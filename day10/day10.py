def get_jolts():
    with open("day10.txt") as f:
        jolts = [int(line) for line in f]
    # add charging outlet
    jolts.append(0)
    # add device's built-in adapter
    jolts.append(max(jolts) + 3)
    jolts.sort()
    return jolts


def part1():
    jolts = get_jolts()
    diffs = {0: 0, 1: 0, 2: 0, 3: 0}
    for i in range(1, len(jolts)):
        d = jolts[i] - jolts[i-1]
        diffs[d] += 1
    return diffs[1] * diffs[3]


def part2():
    jolts = get_jolts()
    counts = [0 for _ in jolts]
    counts[0] = 1
    for i in range(1, len(jolts)):
        rating = jolts[i]
        counts[i] += counts[i-1]
        if i - 2 >= 0 and rating - jolts[i-2] <= 3:
            counts[i] += counts[i-2]
            if i - 3 >= 0 and rating - jolts[i-3] <= 3:
                counts[i] += counts[i-3]
    return counts[-1]


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
    print(f"Part 2:\n{part2()}")
