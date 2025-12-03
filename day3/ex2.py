## Advent of Code day3 : Ex2 - Gauthier Malfilatre

def get_file_lines(filepath: str) -> list[str]:
    """ Return a file lines in a list of str """
    lines: list[str] = []
    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
    except:
        print(f"Cannot read \"{filepath}\".")
    return lines

def biggest_digit(line: str) -> tuple[int, int]:
    """ Find the biggest digit in a str fullfill of digits and its index """
    biggest: int = 0
    bindex : int = -1
    for i, c in enumerate(line):
        if c != '\n' and int(c) > int(biggest):
            biggest = int(c)
            bindex = i
    return bindex + 1, int(biggest)

def biggest_number(line: str, r: int = 2) -> int:
    """ Find the biggest number contained in a str fullfill of int """
    found: str = ""
    index: int = 0
    for i in range(r):
        tindex, digit = biggest_digit(line[index:len(line) - (r - i)])
        if tindex == -1:
            print("Error while parsing")
        found += str(digit)
        index += tindex
    print(found)
    return int(found)

def sum_of_banks(lines: list[str], r: int = 2) -> int:
    """ Find the sum of the biggest joltage of all banks """
    summup: int = 0
    for bank in lines:
        summup += biggest_number(bank, r)
    return summup

if __name__ == "__main__":
    result: int = sum_of_banks(get_file_lines("day3/input.txt"), 12)
    print(result)
