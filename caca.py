## Advent of Code day8 : Ex2 - Gauthier Malfilatre

def get_file_lines(filepath: str) -> list[str]:
    """ Return a file lines in a list of str """
    lines: list[str] = []
    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
    except:
        print(f"Cannot read \"{filepath}\".")
    return lines

def to_xyz(lines: list[str]) -> list[tuple[int]]:
    """ Return the lines but with the expected format XYZ """
    return [tuple([int(j) for j in i[:-1].split(',')]) for i in lines]

def get_distance(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> float:
    """ Get the squared distance using norm of vector """
    return (p2[2] - p1[2]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2

def find_closest_box(boxs: list[tuple[int]], excludes: list[tuple[int, int]] = []) -> tuple[tuple[tuple[int]], tuple[int, int], int]:
    """ Find the closest box's and return a tuple containing the tow closest, there indexs and there distance """
    closest : tuple[tuple[int]] = None
    iclosest: tuple[int, int]   = (0, 0)
    temp    : float             = 0
    for i1, box in enumerate(boxs):
        for i2, box_ in enumerate(boxs):
            if i1 == i2:
                continue
            temp = get_distance(box, box_)
            if (closest == None or temp < closest)  and (i1, i2) not in excludes and (i2, i1) not in excludes:
                closest = temp
                iclosest = (i1, i2)
    return (boxs[iclosest[0]], boxs[iclosest[1]]), iclosest, closest

def sort_reseaus(reseaus: list[list[tuple[int]]]) -> list[list[tuple[int]]]:
    """ Sort reseaux """
    i: int = 0
    while True:
        if i + 1 >= len(reseaus) - 1:
            break
        if len(reseaus[i]) < len(reseaus[i + 1]):
            reseaus[i], reseaus[i + 1] = reseaus[i + 1], reseaus[i]
            i = 0
        else:
            i += 1
    return reseaus

def create_chains(lines: list[tuple[int]]) -> int:
    """ Idk what to write here """
    excludes: list[tuple[int, int]]  = []
    reseaus : list[list[tuple[int]]] = []
    summup  : int                    = 1
    touched : bool                   = False
    indexs  : any                    = None
    j = 0 

    closest, indexs, dis = find_closest_box(lines, [])
    print(closest)
    
    while True:
        if len(reseaus) == 1 and len(reseaus[0]) == len(lines):
            break
        touched = False
    
        closest, indexs, dis = find_closest_box(lines, excludes)
        print(closest, dis)
        if closest == None:
            break
        if not j % 1000:
            print(reseaus, f"\n>>>>>>>>>>>> {len(reseaus)} | {len(excludes)}\n")
        excludes.append(indexs)
        for i, r in enumerate(reseaus):
            if indexs[0] in r and indexs[1] in r:
                touched = True
                break
            if indexs[1] in r:
                stouched = False
                for i_, r_ in enumerate(reseaus):
                    if i == i_:
                        continue
                    if indexs[0] in r_:
                        stouched = True
                        reseaus[i] += r_
                        reseaus.pop(i_)
                        break
                if not stouched:
                    reseaus[i].append(indexs[0])
                touched = True
                break
            if indexs[0] in r:
                stouched = False
                for i_, r_ in enumerate(reseaus):
                    if i_ == i:
                        continue
                    if indexs[1] in r_:
                        stouched = True
                        reseaus[i] += r_
                        reseaus.pop(i_)
                        break
                if not stouched:
                    reseaus[i].append(indexs[1])
                touched = True
                break
        if not touched:
            reseaus.append(list(indexs))
        j += 1

    print(lines[indexs[0]], lines[indexs[1]])
    if len(reseaus) < 3:
        return lines[indexs[0]][0] * lines[indexs[1]][0]
    sort_reseaus(reseaus)
    print(reseaus)
    for i in range(3):
        summup *= len(reseaus[i])
    return summup

if __name__ == "__main__":
    lines: list[str] = get_file_lines("sha.txt")
    lines = to_xyz(lines)
    result: int = create_chains(lines)
    print(result)
