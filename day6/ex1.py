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

def create_ops(lines: list[str]) -> list[list[str]]:
    """ Create more readable operations from lines """
    ops: list[list[str]] = []
    for i, line in enumerate(lines):
        line = line.split()
        if i == 0:
            ops = [[] for _ in range(len(line))]
        for j, term in enumerate(line):
            ops[j].append(term)  
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
