## Advent of Code day6 : Ex1 - Gauthier Malfilatre

def get_file_lines(filepath: str) -> list[str]:
    """ Return a file lines in a list of str """
    lines: list[str] = []
    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
    except:
        print(f"Cannot read \"{filepath}\".")
    return lines

def is_blank(lines: list[str], x: int) -> bool:
    """ Check if a column is blank """
    for i in range(len(lines)):
        if lines[i][x] != ' ':
            return False
    return True

def create_ops(lines: list[str]) -> list[list[str]]:
    """ Create more readable operations from lines """
    ops: list[list[str]] = []
    # Assuming all the lines has the same length
    cop : int = 0
    scop: int = 0
    for i in range(len(lines[0]) - 2, -1, -1):
        if is_blank(lines, i):
            cop += 1
            scop = 0
            continue
        if len(ops) <= cop:
            ops.append([])
        for j in range(len(lines)):
            if lines[j][i] == ' ':
                continue
            if lines[j][i] in ("*", "+"):
                ops[cop].append(lines[j][i])
            else:
                if len(ops[cop]) <= scop:
                    ops[cop].append(lines[j][i])
                else:
                    ops[cop][scop] += lines[j][i]
        scop += 1
    return ops

def do_op(nums: list[str], op: str) -> int:
    """ Recursive shit to do op """
    if not nums or len(nums) < 1:
        return 1 if op == "*" else 0
    if op == "*":
        return int(nums[0]) * do_op(nums[1:], op)
    if op == "+":
        return int(nums[0]) + do_op(nums[1:], op)

def operate(lines: list[str]) -> int:
    """ Process the operation """
    summup: int = 0
    if not lines or len(lines) < 1:
        return summup
    ops: list[list[str]] = create_ops(lines)
    for op in ops:
        summup += do_op(op[:-1], op[-1])
    return summup

if __name__ == "__main__":
    lines: list[str] = get_file_lines("day6/input.txt")
    result: int = operate(lines)
    print(result)
