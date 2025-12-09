## Advent of Code day9 : Ex2 - Gauthier Malfilatre

def get_file_lines(filepath: str) -> list[str]:
    """ Return a file lines in a list of str """
    lines: list[str] = []
    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
    except:
        print(f"Cannot read \"{filepath}\".")
    return lines


def fill_with_green(map_: list[list[int]], lines: list[tuple[int, int]]) -> None:
    """ Fill with green dots """
    for i, tile in enumerate(lines):
        for j, tile_ in enumerate(lines):
            if i == j:
                continue
            if tile[0] == tile_[0]:
                for i in range(tile[1] + 1, tile_[1]):
                    map_[i][tile[0]] = 'X'
            if tile[1] == tile_[1]:
                for i in range(tile[0] + 1, tile_[0]):
                    map_[tile[1]][i] = 'X'

def generate_map(lines: list[tuple[int]]) -> list[list[int]]:
    """  Generate map from lines """
    map_: list[list[int]] = []
    xmax: int = max([i[0] for i in lines])
    ymax: int = max([i[1] for i in lines])
    for y in range(ymax + 2):
        map_.append([])
        for x in range(xmax + 2):
            map_[y].append('.')
    for i in lines:
        map_[i[1]][i[0]] = '#'
    fill_with_green(map_, lines)
    return map_

def get_area(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    """ Get the area of the rectangle """
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

def is_valid(lines: list[tuple[int, int]], x: int, y: int) -> bool:
    """ Check if a rect is valid """
    a: tuple[int] = lines[x]
    b: tuple[int] = (lines[x][0], lines[y][1])
    c: tuple[int] = lines[y]
    d: tuple[int] = (lines[y][0], lines[x][1])
    for i in (b, d):
        checked = [0, 0, 0, 0]
        for j in lines:
            if j[0] <= i[0] and j[1] <= i[1]:
                checked[0] = 1
            if j[0] >= i[0] and j[1] >= i[1]:
                checked[1] = 1
            if j[0] >= i[0] and j[1] <= i[1]:
                checked[2] = 1
            if j[0] <= i[0] and j[1] >= i[1]:
                checked[3] = 1
        if sum(checked) != 4:
            return False
    return True

def find_bsq(lines: list[tuple[int, int]]) -> int:
    """ Find the biggest rectangle """
    indexs: list[tuple[int, int]] = None
    area  : int                   = None
    for i, tile in enumerate(lines):
        for j, tile_ in enumerate(lines):
            if j == i:
                continue
            temp = get_area(tile, tile_)
            if (area == None or temp > area) and is_valid(lines, i, j):
                area = temp
                indexs = (i, j)
    return area, indexs

if __name__ == "__main__":
    lines: list[str] = get_file_lines("day9/input.txt")
    lines = [tuple([int(i) for i in j[:-1].split(',')]) for j in lines]
    result, indexs = find_bsq(lines)
    
    print(lines[indexs[0]], lines[indexs[1]])
    map_ = generate_map(lines)
    map_[lines[indexs[0]][1]][lines[indexs[0]][0]] = '0'
    map_[lines[indexs[1]][1]][lines[indexs[1]][0]] = '0'
    for i in map_:
        for j in i:
            print(j, end="")
        print("\n", end="")
    print(result)
