## Advent of Code day10 : Ex1 - Gauthier Malfilatre

def get_file_lines(filepath: str) -> list[str]:
    """ Return a file lines in a list of str """
    lines: list[str] = []
    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
    except:
        print(f"Cannot read \"{filepath}\".")
    return lines

def lines_to_dict(lines: list[str]) -> dict:
    """ Transform the lines into a dictionnaore """
    nodes: dict = {}
    for line in lines:
        line = line.split(':')
        key = line[0]
        line = line[1].split()
        nodes[key] = [i for i in line]
    return nodes

def count_path(nodes: dict, ckey: str, useskeys: list = [], checker: int = 0) -> int:
    """ Count how many path but in iterative """
    summup: list[int] = [0, 0]
    back: list[list[str, int]] = [[ckey, 0]]
    while back[0] != [ckey, len(nodes[ckey])]:
        if ckey in useskeys:
            back.pop()
            ckey = back[-1][0]
        useskeys.append([ckey, 0])
        if back[-1][1] < len(nodes[ckey]):
            ckey = nodes[ckey][back[-1][1]]
            back[-1][1] += 1
            back.append([ckey, 0])
        else:
            back.pop()
            ckey = back[-1][0]
        if ckey == 'out':
            for i in back:
                if i[0] in ('fft', 'dac'):
                    summup[1] += 1
            if summup[1] == 2:
                summup[0] += 1
            summup[1] = 0
            back.pop()
            ckey = back[-1][0]
    return summup[0]

if __name__ == "__main__":
    lines: list[str] = get_file_lines("day11/input.txt")
    nodes = lines_to_dict(lines)
    result: int = count_path(nodes, 'svr')
    print(result)
