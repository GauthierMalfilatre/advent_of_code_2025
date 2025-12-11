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

def create_lists(lines: list[str]) -> list[list[tuple[int]]]:
    """ Return a list of machines (list of tuples) where:
        -> Tuple at index 0 represente the state the machine must be
        -> Tuples at index 1 ... n - 1 representes the buttons and the leds they toogles
        -> Tuple at index -1 represente the joltage requirement (needed for part 2)
    """
    machines: list[list[tuple[int]]] = []
    for j, machine in enumerate(lines):
        machines.append([])
        for i, pre_tuple in enumerate(machine.split()):
            if i == 0:
                machines[j].append(tuple([1 if c == '#' else 0 for c in pre_tuple[1:][:-1]]))
            else:
                machines[j].append(tuple([int(c) for c in pre_tuple[1:][:-1].replace(",", "") if type(eval(c)) == int]))
    return machines

def press_button(current_state: list[int], b: tuple[int]) -> None:
    """ Active a button """
    for i in b:
        current_state[i] = not current_state[i]

def power_machine(goal: tuple[int], buttons: list[tuple[int]]) -> int:
    """ Power one machine """
    goals        : list[int] = [i for i in range(len(goal)) if goal[i] == 1]
    current_state: list[int] = [0 for _ in goal]
    indexs       : list[int] = []
    shortest     : int       = 0
    clen         : int       = 1
    while True and clen < 1000:
        current_state = [0 for _ in goal]
        for i in range(clen):
            for j, b in enumerate(buttons):
                press_button(current_state, b)
                if tuple(current_state) == goal:
                    return clen
        clen += 1
    return 0

def treate_machines(lines: list[list[tuple[int]]]) -> int:
    """ Treate machines one by one """
    summup: int = 0
    for machine in lines:
        summup += power_machine(machine[0], machine[1:][:-1])
    return summup

if __name__ == "__main__":
    lines: list[str] = get_file_lines("day10/input.txt")
    lines = create_lists(lines)
    result: int = treate_machines(lines)
    print(result)
