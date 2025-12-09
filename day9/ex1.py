## Advent of Code day9 : Ex1 - Gauthier Malfilatre

def get_file_lines(filepath: str) -> list[str]:
    """ Return a file lines in a list of str """
    lines: list[str] = []
    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
    except:
        print(f"Cannot read \"{filepath}\".")
    return lines

def get_area(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    """ Get the area of the rectangle """
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

def find_bsq(lines: list[tuple[int, int]]) -> int:
    """ Find the biggest rectangle """
    indexs: list[tuple[int, int]] = None
    area  : int                   = None
    for i, tile in enumerate(lines):
        for j, tile_ in enumerate(lines):
            if j == i:
                continue
            temp = get_area(tile, tile_)
            if area == None or temp > area:
                area = temp
                indexs = (i, j)
    return area

if __name__ == "__main__":
    lines: list[str] = get_file_lines("day9/input.txt")
    lines = [tuple([int(i) for i in j[:-1].split(',')]) for j in lines]
    result: int = find_bsq(lines)
    print(result)
