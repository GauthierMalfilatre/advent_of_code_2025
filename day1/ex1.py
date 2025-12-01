## Advent of Code day1 : Ex1 - Gauthier Malfilatre

def get_result(filename: str) -> int:
    """ Get the ammount of time the dial is pointing to 0 """
    ammount : int = 0
    position: int = 50
    with open(filename, "r") as f:
        lines = f.readlines()
    for line in lines:
        position += (-1 if line[0] == "L" else 1) * int(line[1:])
        position %= 100
        if position == 0:
            ammount += 1
    return ammount

if __name__ == "__main__":
    result: int = get_result("day1/input.txt")
    print(result)
