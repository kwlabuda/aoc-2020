def get_seat_ids(row_bits, col_bits):
    seat_ids = []
    with open("day5.txt") as f:
        for line in f:
            # row
            row_str = line[:row_bits]
            row = 0
            for i in range(row_bits):
                if row_str[i] == "B":
                    row += 1 << (row_bits - 1 - i)
            # col
            col_str = line[row_bits:row_bits+col_bits]
            col = 0
            for i in range(col_bits):
                if col_str[i] == "R":
                    col += 1 << (col_bits - 1 - i)
            seat_ids.append(row * 8 + col)
    return seat_ids


def part1():
    seat_ids = get_seat_ids(7, 3)
    return max(seat_ids)


def part2():
    row_bits = 7
    col_bits = 3
    seat_ids = set(get_seat_ids(row_bits, col_bits))
    num_seats = (1 << row_bits) * (1 << col_bits)
    # find start of seats
    seat_id = 0
    while seat_id not in seat_ids:
        seat_id += 1
    # next empty seat must be ours
    while seat_id < num_seats:
        if seat_id not in seat_ids:
            return seat_id
        seat_id += 1


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
    print(f"Part 2:\n{part2()}")
