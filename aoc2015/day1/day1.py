from aoc2025.utils.utils import read_input


def star1() -> int:
    data = read_input()
    
    return data[0].count('(') - data[0].count(')')


def star2() -> int:
    data = read_input()
    floor = 0
    for i, v in enumerate(data[0]):
        if v == '(':
            floor += 1
        elif v == ')':
            floor -= 1
        if floor == -1:
            return i + 1
    return 0


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
