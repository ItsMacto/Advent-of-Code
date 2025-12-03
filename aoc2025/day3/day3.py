from aoc2025.utils.utils import read_input
from functools import cache


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

# wow that was easier then i thought
def star2() -> int:
    @cache
    def max_num(nums: tuple[int], num_take: int) -> int:
        if num_take == 0 or not nums or len(nums) < num_take:
            return 0
        
        skip = max_num(nums[1:], num_take)
        take = nums[0] * (10 ** (num_take - 1)) + max_num(nums[1:], num_take - 1)
        return max(skip, take)
    
        
    data = read_input()
    total = 0
    TAKE = 12
    
    for line in data:
        nums = list(map(int, line.strip()))
        large = max_num(tuple(nums), TAKE)
        # print(large)
        total += large
    return total


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")


"""
234234234234278
^^^^^^^^^^^^


"""