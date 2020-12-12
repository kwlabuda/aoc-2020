from collections import Counter
import re

def get_passwords():
    passwords = []
    with open("day2.txt") as f:
        for line in f:
            # parse line
            m = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
            if not m:
                continue
            n1 = int(m.group(1))
            n2 = int(m.group(2))
            letter = m.group(3)
            password = m.group(4)
            passwords.append((n1, n2, letter, password))
    return passwords


def part1():
    valid = 0
    passwords = get_passwords()
    for pw in passwords:
        least, most, letter, password = pw
        # count letters
        c = Counter(password)
        count = c[letter]
        if count >= least and count <= most:
            valid += 1
    return valid


def part2():
    valid = 0
    passwords = get_passwords()
    for pw in passwords:
        idx1, idx2, letter, password = pw
        # check
        a = password[idx1 - 1]
        b = password[idx2 - 1]
        if a != b and (a == letter or b == letter):
            valid += 1
    return valid


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
    print(f"Part 2:\n{part2()}")
