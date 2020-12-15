def get_numbers():
    with open("day15.txt") as f:
        text = f.read()
        return [int(n) for n in text.split(",")]


def find_number(target):
    numbers = get_numbers()
    # create dictionary to store number positions
    history = {n: t for t, n in enumerate(numbers[:-1])}
    # check numbers until target reached
    t = len(numbers)
    prev = numbers[-1]
    while t < target:
        n = 0
        if prev in history:
            n = t - 1 - history[prev]
        history[prev] = t - 1
        prev = n
        t += 1
    return prev


if __name__ == "__main__":
    print(f"Part 1:\n{find_number(2020)}")
    print(f"Part 2:\n{find_number(30000000)}")
