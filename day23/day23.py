def play(cups, rounds):
    # create linked list
    links = [0] * (len(cups) + 1)
    for i in range(len(cups) - 1):
        curr_cup = cups[i]
        next_cup = cups[i + 1]
        links[curr_cup] = next_cup
    links[cups[-1]] = cups[0]
    # play rounds
    min_cup = min(cups)
    max_cup = max(cups)
    curr_cup = cups[0]
    for _ in range(rounds):
        # get next 3 cups
        next_cups = [links[curr_cup]]
        next_cups.append(links[next_cups[0]])
        next_cups.append(links[next_cups[1]])
        # get destination
        dst_cup = curr_cup - 1
        if dst_cup < min_cup:
            dst_cup = max_cup
        while dst_cup in next_cups:
            dst_cup -= 1
            if dst_cup < min_cup:
                dst_cup = max_cup
        # insert cups at destination
        links[curr_cup] = links[next_cups[2]]
        temp = links[dst_cup]
        links[dst_cup] = next_cups[0]
        links[next_cups[2]] = temp
        # select new current cup
        curr_cup = links[curr_cup]
    return links


def part1():
    labeling = "712643589"
    cups = [int(c) for c in labeling]
    links = play(cups, 100)
    # get string
    cups = []
    c = 1
    while (links[c] != 1):
        c = links[c]
        cups.append(c)
    return "".join(str(c) for c in cups)


def part2():
    labeling = "712643589"
    cups = [int(c) for c in labeling]
    cups += list(range(max(cups) + 1, 1000001))
    links = play(cups, 10000000)
    # get cups after 1
    cup1 = links[1]
    cup2 = links[cup1]
    return cup1 * cup2


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
    print(f"Part 2:\n{part2()}")
