import re

DIRECTIONS = {
    "ne": (1, 1),
    "nw": (-1, 1),
    "se": (1, -1),
    "sw": (-1, -1),
    "e": (2, 0),
    "w": (-2, 0)
}

#    / \ / \
#   |   |   |
#  / \ / \ / \
# |   |   |   |
#  \ / \ / \ /
#   |   |   |
#    \ / \ /

def get_tile_list():
    with open("day24.txt") as f:
        return [re.findall(r"ne|nw|se|sw|e|w", line) for line in f]


def renovate_floor():
    tile_list = get_tile_list()
    black_tiles = set()
    for directions in tile_list:
        x, y = 0, 0
        for d in directions:
            move = DIRECTIONS[d]
            x += move[0]
            y += move[1]
        pos = (x, y)
        if pos in black_tiles:
            black_tiles.remove(pos)
        else:
            black_tiles.add(pos)
    return black_tiles


def part1():
    black_tiles = renovate_floor()
    return len(black_tiles)


def get_adjacent_white(tile, black_tiles):
    x, y = tile
    adj_white = []
    for move in DIRECTIONS.values():
        pos = (x + move[0], y + move[1])
        if pos not in black_tiles:
            adj_white.append(pos)
    return adj_white


def part2():
    # get initial set of black tiles
    black_tiles = renovate_floor()
    # flip tiles over 100 days
    for _ in range(100):
        # go through black tiles
        new_black_tiles = set()
        white_tiles = set()
        for tile in black_tiles:
            adj_white = get_adjacent_white(tile, black_tiles)
            num_black = 6 - len(adj_white)
            if num_black != 0 and num_black <= 2:
                new_black_tiles.add(tile)
            # add any white tiles
            white_tiles.update(adj_white)
        # go through white tiles
        for tile in white_tiles:
            adj_white = get_adjacent_white(tile, black_tiles)
            num_black = 6 - len(adj_white)
            if num_black == 2:
                new_black_tiles.add(tile)
        black_tiles = new_black_tiles
    return len(black_tiles)


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
    print(f"Part 2:\n{part2()}")
