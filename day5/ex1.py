## Advent of Code day5 : Ex1 - Gauthier Malfilatre

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

def count_valid_ids(lines: list[str]) -> int:
    """ Count valids ids that are in ranges """
    summump: int = 0
    if not lines or len(lines) < 1:
        return summump
    ranges : list[tuple[int, int]] = get_ranges(lines)
    ids    : list[int]             = get_ids(lines) 

    for id in ids:
        for r in ranges:
            if r[0] <= id <= r[1]:
                summump += 1
                break
    return summump

if __name__ == "__main__":
    lines: list[str] = get_file_lines("day5/input.txt")
    result: int = count_valid_ids(lines)
    print(result)
