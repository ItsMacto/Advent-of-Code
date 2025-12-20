from aoc2025.utils.utils import read_input


def star1() -> int:
    data = read_input()
    lights = [[False for _ in range(1000)] for _ in range(1000)]
    for line in data:
        parts = line.split()
        if parts[0] == "toggle":
            x1, y1 = map(int, parts[1].split(","))
            x2, y2 = map(int, parts[3].split(","))
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[x][y] = not lights[x][y]
        else:
            action = parts[1]
            x1, y1 = map(int, parts[2].split(","))
            x2, y2 = map(int, parts[4].split(","))
            turn_on = action == "on"
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[x][y] = turn_on
    count = sum(sum(1 for light in row if light) for row in lights)
    return count
        

def star2() -> int:
    data = read_input()
    lights = [[0] * 1000 for _ in range(1000)]
    for line in data:
        parts = line.split()
        if parts[0] == "toggle":
            x1, y1 = map(int, parts[1].split(","))
            x2, y2 = map(int, parts[3].split(","))
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[x][y] += 2
        else:
            action = parts[1]
            x1, y1 = map(int, parts[2].split(","))
            x2, y2 = map(int, parts[4].split(","))
            turn_on = action == "on"
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[x][y] += 1 if turn_on else -1
                    lights[x][y] = max(0, lights[x][y])
    count = sum(sum(light for light in row) for row in lights)
    return count


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
