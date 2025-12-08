## Advent of Code day7 : Ex1 - Gauthier Malfilatre

def get_file_lines(filepath: str) -> list[str]:
    """ Return a file lines in a list of str """
    lines: list[str] = []
    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
    except:
        print(f"Cannot read \"{filepath}\".")
    return lines

def chillbro(lines: list[list[int]], x: int, y: int) -> int:
    """ Bro idk how to name this func bro i swear """
    if lines[y][x] != '|':
        return 0
    if y + 1 >= len(lines):
        return 0 
    if lines[y + 1][x] == '^':
        lines[y + 1][x + 1] = '|'
        lines[y + 1][x - 1] = '|'
        return 1
    else:
        lines[y + 1][x] = '|'
        return 0

def manifold(lines: list[str]) -> int:
    """ Process and run beam """
    summup: int = 0
    lines = [[i for i in line] for line in lines]
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == 'S':
                lines[y + 1][x] = "|"
            summup += chillbro(lines, x, y)
    return summup

if __name__ == "__main__":
    lines: list[str] = get_file_lines("day7/input.txt")
    result: int = manifold(lines)
    print(result)
