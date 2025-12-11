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

def count_path(nodes: dict, ckey: str, useskeys: list) -> int:
    summup: int = 0
    if ckey == 'out':
        return 1
    if ckey in useskeys:
        return 0
    for i in nodes[ckey]:
        summup += count_path(nodes, i, useskeys + [ckey,])
    return summup

if __name__ == "__main__":
    lines: list[str] = get_file_lines("day11/input.txt")
    nodes = lines_to_dict(lines)
    print(nodes)
    result: int = count_path(nodes, 'you', [])
    print(result)
