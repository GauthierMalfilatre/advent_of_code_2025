## Advent of Code day4 : Ex2 - Gauthier Malfilatre

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

def how_many_rolls(map_: list[str], limit: int = 4) -> tuple[int, list[tuple[int, int]]]:
    """ Return how many rolls elves can access """
    positions: list[tuple[int, int]] = []
    summup: int = 0
    if not map_ or len(map_) < 1:
        return summup
    for y, row in enumerate(map_):
        for x, col in enumerate(row):
            if count_neighbors(map_, x, y) < limit:
                summup += 1
                positions.append((x, y))
    return summup, positions

if __name__ == "__main__":
    positions: list[tuple[int, int]] = [1]
    result: int = 0
    map_: list[str] = get_file_lines("day4/input.txt")
    while len(positions) > 0:
        tresult, positions = how_many_rolls(map_, 4)
        result += tresult
        for i in positions:
            map_[i[1]] = list(map_[i[1]])
            map_[i[1]][i[0]] = '.'
            map_[i[1]] = "".join(map_[i[1]])
    print(result)
