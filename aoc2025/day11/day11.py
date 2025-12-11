from aoc2025.utils.utils import read_input


def star1() -> int:
    data = read_input()
    devices = {}
    for line in data:
        key, values = line.split(":")
        values = values.split()
        devices[key] = values
        
    START = "you"
    END = "out"
    def dfs(curr):
        if curr == END:
            return 1
        x = 0
        for val in devices[curr]:
            x += dfs(val)
        return x
    num_paths = dfs(START)
    return num_paths


def star2() -> int:
    data = read_input()
    # data = read_input(test=True)
    devices = {}
    for line in data:
        key, values = line.split(":")
        values = values.split()
        devices[key] = values
        
    memo = {}
    def dfs(curr, target):
        if curr in memo:
            return memo[curr]
        if curr == target:
            return 1
        if curr not in devices:
            return 0
        x = 0
        for val in devices[curr]:
            x += dfs(val, target)
        memo[curr] = x
        return x
    p1 = dfs('svr', 'fft')
    memo = {}
    p2 = dfs('fft', 'dac')
    memo = {}
    p3 = dfs('dac', 'out')
    # print(p1, p2, p3)
    num_paths = p1 * p2 * p3
    return num_paths


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
