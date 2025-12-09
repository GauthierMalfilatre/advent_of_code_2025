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
        map_[i[1]][i[0]] = i[2]
#    fill_with_green(map_, lines)
    return map_

def get_area(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    """ Get the area of the rectangle """
    x1, y1, t = p1
    x2, y2, t = p2
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

def is_valid2(lines: list[tuple[int, int]], x: int, y: int) -> bool:
    """ is valid 2 (new approch) """
    a: tuple[int] = lines[x]
    b: tuple[int] = (lines[x][0], lines[y][1], '#')
    c: tuple[int] = lines[y]
    d: tuple[int] = (lines[y][0], lines[x][1], '#')
    for p in (a, b, c, d):
        xfounds = []
        yfounds = []
        xcount: int = 0
        ycount: int = 0
        xcount_: int = 0
        ycount_: int = 0
        for i in lines:
            if i[0] < p[0] and i[0] not in xfounds:
#                print("P1", i[0], p[0])
                xcount += 1
                xfounds.append(i[0])
            if i[1] < p[1] and i[1] not in yfounds:
                ycount += 1
#                print("P1", i[1], p[1])
                yfounds.append(i[1])
            if i[0] > p[0] and i[0] not in xfounds:
#                print("P1", i[0], p[0])
                xcount_ += 1
                xfounds.append(i[0])
            if i[1] > p[1] and i[1] not in yfounds:
                ycount_ += 1
#                print("P1", i[1], p[1])
                yfounds.append(i[1])
#        print(p, xcount, ycount, xcount_, ycount_)
        if not p in lines and (xcount % 2 != 0 or ycount % 2 != 1):
            return False
        if not p in lines and (xcount_ % 2 != 1 or ycount_ % 2 != 0 or ycount_ < 1 or xcount_ < 1):
            return False
    return True

def find_bsq(lines: list[tuple[int, int]]) -> int:
    """ Find the biggest rectangle """
    indexs: list[tuple[int, int]] = None
    area  : int                   = None
    for i, tile in enumerate(lines):
        if tile[2] != '#':
            continue
        for j, tile_ in enumerate(lines):
            if j == i or tile_[2] != '#':
                continue
            temp = get_area(tile, tile_)
            if (area == None or temp > area) and is_valid2(lines, i, j):
                area = temp
                indexs = (i, j)
    return area, indexs

def add_green_tiles(lines: list[tuple[int]]) -> None:
    """ Fill with green tiles """
    i = 0
    lines.append(lines[0])
    while i < len(lines) - 1:
        if lines[i][2] == '#':
            if lines[i][0] == lines[i + 1][0]:
                a, b = lines[i][1], lines[i + 1][1]
                if lines[i][1] > lines[i + 1][1]:
                    a, b = b, a
                for j in range(a + 1, b):
                    lines.insert(i + 1, (lines[i][0], j, 'X'))
                    i += 1
            if lines[i][1] == lines[i + 1][1]:
                a, b = lines[i][0], lines[i + 1][0]
                if lines[i][0] > lines[i + 1][0]:
                    a, b = b, a
                for j in range(a + 1, b):
                    lines.insert(i + 1, (j, lines[i][1], 'X'))
                    i += 1
        i += 1

if __name__ == "__main__":
    lines: list[str] = get_file_lines("day9/input.txt")
    lines = [tuple([int(i) for i in j[:-1].split(',')]+['#',]) for j in lines]
    # add_green_tiles(lines)
    result, indexs = find_bsq(lines)
    """
    map_ = generate_map(lines)
    map_[lines[indexs[0]][1]][lines[indexs[0]][0]] = '0'
    map_[lines[indexs[1]][1]][lines[indexs[1]][0]] = '0'
    for i in map_:
        for j in i:
            print(j, end="")
        print("\n", end="")
    is_valid2(lines, indexs[0], indexs[1])
    """
    print(result)
