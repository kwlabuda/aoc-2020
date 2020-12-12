import re

PREAMBLE = 25

def get_numbers():
    with open("day9.txt") as f:
        return [int(line) for line in f]


def check_sum(numbers, num):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == num:
                return True
    return False


def part1():
    nums = get_numbers()
    prev_nums = nums[:PREAMBLE]
    for num in nums[PREAMBLE:]:
        if not check_sum(prev_nums, num):
            return num
        prev_nums.pop(0)
        prev_nums.append(num)


def part2():
    nums = get_numbers()
    bad_num = part1()
    right = 0
    total = nums[0]
    for left in range(len(nums)):
        while total < bad_num:
            right += 1
            total += nums[right]
        while total > bad_num:
            total -= nums[right]
            right -= 1
        if total == bad_num:
            subset = nums[left:right+1]
            return min(subset) + max(subset)
        total -= nums[left]
    raise Exception("Cannot find range")


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
    print(f"Part 2:\n{part2()}")
