## Advent of Code day2 : Ex1 - Gauthier Malfilatre

def get_file_content(filepath: str) -> str:
    """ Get the plain text contained in a file """
    to_return: str = None
    with open(filepath, "r") as f:
        to_return = f.read()
    return to_return

def is_valid(id: int) -> bool:
    """ Check if the given id is valid """
    prev: str = ""
    id_ = str(id)
    for index, c in enumerate(id_):
        if id_[index:] == prev:
            return False
        prev += c
    return True

def get_sum_of_invalid_ids(filepath: str) -> int:
    """ Get the sum of the invalid ids in the given range """
    sigma       : int = 0
    id_range_str: str = get_file_content(filepath)
    if id_range_str == None:
        print(f"Enable to open {filepath}")
        return 0
    id_range    : list[str] = id_range_str.split(",")

    for i in id_range:
        tranges: list[str] = i.split("-")
        for id in range(int(tranges[0]), int(tranges[1]) + 1):  # +1 to include
            if not is_valid(id):
                sigma += id
    return sigma

if __name__ == "__main__":
    result = get_sum_of_invalid_ids("day2/input.txt")
    print(result)
