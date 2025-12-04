## Advent of Code day4 : Ex1 - Gauthier Malfilatre

def get_file_lines(filepath: str) -> list[str]:
    """ Return a file lines in a list of str """
    lines: list[str] = []
    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
    except:
        print(f"Cannot read \"{filepath}\".")
    return lines

def count_neighbors(map_: list[str], x: int, y: int) -> int:
    """ Count the number of neighbors in the height adjacent positions if valids"""
    neighbors: int = 0
    pos: tuple[tuple[int, int]] = (
        (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)
    )
    if map_[y][x] != "@":
        return 10
    for p in pos:
        if not (0 <= y + p[1] < len(map_)) or not (0 <= x + p[0] < len(map_[y + p[1]])):
            continue
        if map_[y + p[1]][x + p[0]] == "@":
            neighbors += 1
    return neighbors

def how_many_rolls(map_: list[str], limit: int = 4) -> int:
    """ Return how many rolls elves can access """
    summup: int = 0
    if not map_ or len(map_) < 1:
        return summup
    for y, row in enumerate(map_):
        for x, col in enumerate(row):
            if count_neighbors(map_, x, y) < limit:
                summup += 1
    return summup

if __name__ == "__main__":
    result: int = how_many_rolls(get_file_lines("day4/input.txt"), 4)
    print(result)
