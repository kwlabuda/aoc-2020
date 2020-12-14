import re

def get_data():
    with open("day14.txt") as f:
        return [line.strip() for line in f]


def part1():
    lines = get_data()
    and_mask = 0
    or_mask = 0
    memory = {}
    for line in lines:
        if line.startswith("mask"):
            # get new bitmask
            bitmask = re.search(r"[X01]+", line).group(0)
            and_mask = int("".join("0" if c == "0" else "1" for c in bitmask), 2)
            or_mask = int("".join("1" if c == "1" else "0"for c in bitmask), 2)
        elif line.startswith("mem"):
            # memory write
             m = re.search(r"\[(\d+)\] = (\d+)", line)
             addr = int(m.group(1))
             val = int(m.group(2))
             memory[addr] = (val & and_mask) | or_mask
    return sum(memory.values())


def part2():
    lines = get_data()
    bitmask = None
    memory = {}
    for line in lines:
        if line.startswith("mask"):
            # get new bitmask
            bitmask = re.search(r"[X01]+", line).group(0)
        elif line.startswith("mem"):
            # get address and value
            m = re.search(r"\[(\d+)\] = (\d+)", line)
            addr = int(m.group(1))
            val = int(m.group(2))
            # apply mask to address
            addr_bits = list(f"{addr:0>36b}")
            for i in range(len(bitmask)):
                if bitmask[i] == "1":
                    addr_bits[i] = "1"
                elif bitmask[i] == "X":
                    addr_bits[i] = "X"
            bits_str = "".join(addr_bits)
            # write to each possible address
            stack = [bits_str]
            while len(stack) > 0:
                bs = stack.pop()
                if "X" in bs:
                    stack.append(bs.replace("X", "0", 1))
                    stack.append(bs.replace("X", "1", 1))
                else:
                    a = int(bs, 2)
                    memory[a] = val
    return sum(memory.values())


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
    print(f"Part 2:\n{part2()}")
