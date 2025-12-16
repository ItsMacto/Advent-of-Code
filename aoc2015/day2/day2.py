from aoc2025.utils.utils import read_input


def star1() -> int:
    data = read_input()
    total = 0
    for line in data:
        x, y, z = map(int, line.split('x'))
        small_side = min(x*y, x*z, y*z)
        total += small_side + 2*x*y +2*x*z + 2* y*z
    

    return total


def star2() -> int:
    data = read_input()
    total = 0
    for line in data:
        x, y, z = map(int, line.split('x'))
        perimeter = 2* min(x+y, x+z, z+y)
        total +=  perimeter + x*y*z
    return total


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
