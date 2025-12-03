from aoc2025.utils.utils import read_input


def star1() -> int:
    data = read_input()
    total = 0
    for line in data:
        highest = 0
        l, r = 0, 1
        while r < len(line):
            num = int(line[l] + line[r])
            if num > highest:
                highest = num
            if int(line[r]) > int(line[l]):
                l = r
            r += 1
        # print(highest)
        total += highest
    return total


def star2() -> int:
    # data = read_input(test=True)
    # total = 0
    # for line in data:
    #     least_pos = -1
    #     nums = []
    #     for n in range(12):
    #         for i in range(len(line) -1, least_pos, -1):
                
        
        
    return 0


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")


"""
234234234234278
^^^^^^^^^^^^


"""