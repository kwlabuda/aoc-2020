def get_numbers():
    with open("day1.txt") as f:
        return [int(line) for line in f]


def part1():
    numbers = get_numbers()
    length = len(numbers)
    for i in range(length):
        for j in range(i + 1, length):
            if numbers[i] + numbers[j] == 2020:
                return numbers[i] * numbers[j]


def part2():
    numbers = get_numbers()
    length = len(numbers)
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                a = numbers[i]
                b = numbers[j]
                c = numbers[k]
                if a + b + c == 2020:
                    return a * b * c


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
    print(f"Part 2:\n{part2()}")
