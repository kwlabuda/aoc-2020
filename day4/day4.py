import re

FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def get_passports():
    with open("day4.txt") as f:
        text = f.read()
    return re.split(r"\n{2,}", text)


def part1():
    passports = get_passports()
    valid_count = 0
    for pp in passports:
        is_valid = True
        for field in FIELDS:
            if field + ":" not in pp:
                is_valid = False
                break
        if is_valid:
            valid_count += 1
    return valid_count


def is_passport_valid(pp):
    # birth year
    m = re.search(r"byr:(\d{4})\b", pp)
    if not m:
        return False
    year = int(m.group(1))
    if year < 1920 or year > 2002:
        return False
    # issue year
    m = re.search(r"iyr:(\d{4})\b", pp)
    if not m:
        return False
    year = int(m.group(1))
    if year < 2010 or year > 2020:
        return False
    # exp year
    m = re.search(r"eyr:(\d{4})\b", pp)
    if not m:
        return False
    year = int(m.group(1))
    if year < 2020 or year > 2030:
        return False
    # height
    m = re.search(r"hgt:(\d+)(cm|in)", pp)
    if not m:
        return False
    h = int(m.group(1))
    unit = m.group(2)
    if unit == "cm":
        if h < 150 or h > 193:
            return False
    elif unit == "in":
        if h < 59 or h > 76:
            return False
    # hair
    m = re.search(r"hcl:#[0-9a-f]{6}\b", pp)
    if not m:
        return False
    # eyes
    m = re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)\b", pp)
    if not m:
        return False
    # id
    m = re.search(r"pid:\d{9}\b", pp)
    if not m:
        return False
    # valid
    return True


def part2():
    passports = get_passports()
    valid_count = 0
    for pp in passports:
        if is_passport_valid(pp):
            valid_count += 1
    return valid_count


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
    print(f"Part 2:\n{part2()}")
