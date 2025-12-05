## Advent of Code day5 : Ex2 - Gauthier Malfilatre

def get_file_lines(filepath: str) -> list[str]:
    """ Return a file lines in a list of str """
    lines: list[str] = []
    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
    except:
        print(f"Cannot read \"{filepath}\".")
    return lines

def get_ranges(lines: list[str]) -> list[tuple[int, int]]:
    """ Get ranges from base lines """
    ranges: list[tuple[int, int]] = []
    for line in lines:
        if line == "\n":
            break
        ranges.append([int(i) for i in line.split("-")])
    return ranges

def get_ids(lines: list[str]) -> list[int]:
    """ Get ids from base lines """
    ids: list[int] = []
    for line in lines:
        if '-' in line:
            continue
        if line == "\n":
            continue
        ids.append(int(line))
    return ids

def sort_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """ Sort the ranges base on their size """
    nranges: list[tuple[int, int]] = ranges
    i      : int = 0
    while i < len(nranges) - 1:
        if nranges[i][1] - nranges[i][0] < nranges[i + 1][1] - nranges[i + 1][0]:
            nranges[i], nranges[i + 1] = nranges[i + 1], nranges[i]
            i = 0
        else:
            i += 1
    return nranges

def merge_ranges(ranges: list[tuple[int, int]]) -> tuple[list[tuple[int, int]], bool]:
    """ Merge the ranges so it wille be faster and easier to calculate fresh ones """
    nranges: list[tuple[int, int]] = []
    ismod  : bool = False
    touched: bool = False
    print("caca")
    for i, r in enumerate(ranges):
        ismod = False
        for ni, nr in enumerate(nranges):
            if r[0] < nr[0] and r[1] >= nr[0]:
                nranges[ni][0] = r[0]
                ismod = True
                touched = True
            if r[1] > nr[1] and r[0] <= nr[1]:
                nranges[ni][1] = r[1]
                ismod = True
                touched = True
            if r[0] >= nr[0] and r[1] <= nr[1]:
                ismod = True
            if ismod:
                break
        if not ismod:
            nranges.append(r)
    return nranges, touched

def count_valid_ids(lines: list[str]) -> int:
    """ Count valids ids that are in ranges """
    summump: int = 0
    if not lines or len(lines) < 1:
        return summump
    ranges : list[tuple[int, int]] = get_ranges(lines)
    ids    : list[int]             = get_ids(lines) 
    ranges = sort_ranges(ranges)
    while True:
        ranges, touch = merge_ranges(ranges)
        if not touch:
            break
    print(ranges)
    for i in ranges:
        summump += len(range(i[0], i[1] + 1))
    return summump

if __name__ == "__main__":
    lines: list[str] = get_file_lines("day5/input.txt")
    result: int = count_valid_ids(lines)
    print(result)
