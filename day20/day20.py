import math
import re

class Tile():

    def __init__(self, text):
        lines = text.split("\n")
        m = re.search(r"\d+", lines[0])
        self.tid = int(m.group(0))
        self.pixels = lines[1:]
        self.get_edges()
        self.neighbors = []

    def __eq__(self, other):
        return self.tid == other.tid

    def __str__(self):
        return "\n".join(self.pixels)

    def get_edges(self):
        T = self.pixels[0]
        R = "".join(row[-1] for row in self.pixels)
        B = self.pixels[-1][::-1]
        L = "".join(row[0] for row in self.pixels[::-1])
        self.edges = [T, R, B, L]

    def fits_tile(self, tile):
        if self.tid == tile.tid:
            return False
        for i, e1 in enumerate(self.edges):
            for j, e2 in enumerate(tile.edges):
                if e1 == e2 or e1 == e2[::-1]:
                    self.neighbors.append([i, tile, j, e1 == e2])
                    return True
        return False

    def rotate(self):
        self.pixels = rotate_grid(self.pixels)
        self.get_edges()
        for n in self.neighbors:
            n[0] = (n[0] + 1) % 4

    def flip_x(self):
        self.pixels = [row[::-1] for row in self.pixels]
        self.get_edges()
        for n in self.neighbors:
            if n[0] % 2 == 1:
                n[0] = (n[0] + 2) % 4
            n[3] = not n[3]

    def flip_y(self):
        self.pixels = self.pixels[::-1]
        self.get_edges()
        for n in self.neighbors:
            if n[0] % 2 == 0:
                n[0] = (n[0] + 2) % 4
            n[3] = not n[3]

    def get_neighbor(self, side):
        for n in self.neighbors:
            if n[0] == side:
                return n
        raise ValueError(f"Tile has no neighbor on side {side}")

    def fit_neighbor(self, side):
        _, t, j, b = self.get_neighbor(side)
        if b is True:
            if j % 2 == 0:
                t.flip_x()
            else:
                t.flip_y()
        flips = (side + 2 - j) % 4
        for _ in range(flips):
            t.rotate()
        return t

    def no_border(self):
        return [row[1:-1] for row in self.pixels[1:-1]]


def get_tiles():
    with open("day20.txt") as f:
        text = f.read().strip()
    tile_strs = re.split(r"\n{2,}", text)
    return [Tile(s) for s in tile_strs]


def part1():
    tiles = get_tiles()
    corners = []
    for tile in tiles:
        count = sum(1 for t in tiles if tile.fits_tile(t))
        if count == 2:
            corners.append(tile)
    if len(corners) != 4:
        raise Exception("Expected 4 corners")
    product = 1
    for tile in corners:
        product *= tile.tid
    return product


def draw_grid(grid):
    h = len(grid[0][0])
    rows = []
    for row in grid:
        for y in range(h):
            rows.append("".join(tile[y] for tile in row))
    return rows


def rotate_grid(grid):
    return [
        "".join(row[i] for row in grid[::-1])
        for i, row in enumerate(grid)
    ]


def count_monsters(grid, mon_coords, x_end, y_end):
    count = 0
    for y in range(y_end):
        line = grid[y]
        for x in range(x_end):
            found = True
            # check each hash in sea monster
            for u, v in mon_coords:
                if grid[y + v][x + u] != "#":
                    found = False
                    break
            if found is True:
                count += 1
    return count


def part2():
    tiles = get_tiles()
    side_len = int(math.sqrt(len(tiles)))

    # verify tile match counts and find corners
    corners = []
    for tile in tiles:
        count = sum(1 for t in tiles if tile.fits_tile(t))
        if count == 2:
            corners.append(tile)
        elif count < 2 or count > 4:
            raise Exception("Tile should fit 2-4 other tiles")

    # choose a corner to be top left
    corner = corners.pop()
    while (
        corner.neighbors[0][0] in {0, 3}
        or corner.neighbors[1][0] in {0, 3}
    ):
        corner.rotate()

    # construct grid of tiles
    grid = []
    for y in range(side_len):
        row = None
        # get first tile of row
        if y == 0:
            row = [corner]
        else:
            prev = grid[-1][0]
            t = prev.fit_neighbor(2)
            row = [t]
        for x in range(1, side_len):
            # for each tile
            prev = row[-1]
            t = prev.fit_neighbor(1)
            row.append(t)
        grid.append(row)

    # remove borders from tiles
    grid = [[tile.no_border() for tile in row] for row in grid]
    grid = draw_grid(grid)

    # find sea monsters
    SEA_MONSTER = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   "
    ]
    mon_coords = []
    for y, line in enumerate(SEA_MONSTER):
        for x, char in enumerate(line):
            if char == "#":
                mon_coords.append((x, y))
    x_end = len(grid[0]) - len(SEA_MONSTER[0])
    y_end = len(grid) - len(SEA_MONSTER)
    # check normal and flipped
    for _ in range(2):
        # check each rotation
        for _ in range(4):
            count = count_monsters(grid, mon_coords, x_end, y_end)
            if count > 0:
                grid_count = "".join(grid).count("#")
                monster_count = "".join(SEA_MONSTER).count("#") * count
                return grid_count - monster_count
            grid = rotate_grid(grid)
        grid = grid[::-1]


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
    print(f"Part 2:\n{part2()}")
