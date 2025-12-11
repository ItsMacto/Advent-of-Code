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
    data = read_input(test=True)
    # TODO: Implement star 2 solution
    return 0


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
