DIRECTIONS = [
    (-1, -1), (0, -1), (1, -1),
    (-1,  0),          (1,  0),
    (-1,  1), (0,  1), (1,  1)
]

def get_seats():
    with open("day11.txt") as f:
        return [[c for c in line.strip()] for line in f]


def is_occupied(seats, w, h, x, y, dx, dy, adjacent):
    while True:
        x += dx
        y += dy
        if x < 0 or x >= w or y < 0 or y >= h:
            return False
        if seats[y][x] == "L":
            return False
        if seats[y][x] == "#":
            return True
        # only check once if adjacent
        if adjacent is True:
            return False


def get_occupancy(adjacent, empty_threshold):
    seats = get_seats()
    h = len(seats)
    w = len(seats[0])
    prev_occupancy = 0

    while (True):
        new_seats = [list(row) for row in seats]
        for y in range(h):
            for x in range(w):
                seat = seats[y][x]
                # skip spaces with no seats
                if seat == ".":
                    continue
                # count occupied seats
                occupied = 0
                for d in DIRECTIONS:
                    if is_occupied(seats, w, h, x, y, d[0], d[1], adjacent):
                        occupied += 1
                # reassign seat
                if occupied == 0:
                    new_seats[y][x] = "#"
                elif seat == "#" and occupied >= empty_threshold:
                    new_seats[y][x] = "L"

        # check previous occupancy
        new_occupancy = sum(row.count("#") for row in new_seats)
        if new_occupancy != prev_occupancy:
            seats = new_seats
            prev_occupancy = new_occupancy
        else:
            return new_occupancy


if __name__ == "__main__":
    print(f"Part 1:\n{get_occupancy(True, 4)}")
    print(f"Part 2:\n{get_occupancy(False, 5)}")
