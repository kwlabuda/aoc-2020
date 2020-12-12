def get_instructions():
    with open("day12.txt") as f:
        return [(line[0], int(line[1:])) for line in f]


def part1():
    instructions = get_instructions()
    NS = 0
    EW = 0
    angle = 90
    for act, num in instructions:
        if act == "N":
            NS += num
        elif act == "S":
            NS -= num
        elif act == "E":
            EW += num
        elif act == "W":
            EW -= num
        elif act == "L":
            angle = (angle - num) % 360
        elif act == "R":
            angle = (angle + num) % 360
        elif act == "F":
            if angle == 0:
                NS += num
            elif angle == 90:
                EW += num
            elif angle == 180:
                NS -= num
            elif angle == 270:
                EW -= num
            else:
                raise Exception("Invalid angle")
    return NS, EW, abs(NS) + abs(EW)


def part2():
    instructions = get_instructions()
    NS = 0
    EW = 0
    wp_NS = 1
    wp_EW = 10
    for act, num in instructions:
        if act == "N":
            wp_NS += num
        elif act == "S":
            wp_NS -= num
        elif act == "E":
            wp_EW += num
        elif act == "W":
            wp_EW -= num
        elif act == "L" or act == "R":
            if act == "L":
                num = 360 - num
            if num == 90:
                t = wp_NS
                wp_NS = -wp_EW
                wp_EW = t
            elif num == 180:
                wp_EW = -wp_EW
                wp_NS = -wp_NS
            elif num == 270:
                t = wp_EW
                wp_EW = -wp_NS
                wp_NS = t
            else:
                raise Exception("Invalid turn")
        elif act == "F":
            NS += wp_NS * num
            EW += wp_EW * num
    return NS, EW, abs(NS) + abs(EW)


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
    print(f"Part 2:\n{part2()}")
