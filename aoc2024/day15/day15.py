from aoc2025.utils.utils import read_input, grid_print, grid_find, to_grid, grid_find_all
from collections import deque

def push(grid, location, direction):
    x, y = location
    dx, dy = direction
    nx, ny = x + dx, y + dy
    if grid[ny][nx] == ".":
        # Move
        grid[y][x] = "."
        grid[y + dy][x + dx] = "@"
        return (x + dx, y + dy)
    elif grid[ny][nx] == "#":
        # Stop
        return location
    elif grid[ny][nx] == "O":
        count = 0
        while grid[ny][nx] == "O":
            nx += dx
            ny += dy
            count += 1
        # print("count", count)
        if grid[ny][nx] == ".":
            # Move
            grid[y][x] = "."
            grid[y + dy][x + dx] = "@"
            for step in range(2, count + 2):
                # print(y + dy * step, x + dx * step)
                grid[y + dy * step][x + dx * step] = "O"
            return (x + dx, y + dy)
    else:
        raise ValueError(f"Invalid grid cell: {grid[ny][nx]}")
            

def star1() -> int:
    data = read_input()
    grid = []
    instructions = []
    line_count = 0
    for line in data:
        if line_count < 2:
            grid.append(line)
            if set(line) == {"#"}:
                line_count += 1
        else:
            for char in line:
                instructions.append(char)
    grid = to_grid(grid)
    # print(instructions)
    for instr in instructions:
        # grid_print(grid)
        # print(instr)
        location = grid_find(grid, "@")
        # print(location)
        if instr == "<":
            push(grid, location, (-1, 0))
        elif instr == ">":
            push(grid, location, (1, 0))
        elif instr == "^":
            push(grid, location, (0, -1))
        elif instr == "v":
            push(grid, location, (0, 1))

    # grid_print(grid)
    total = 0
    locations = grid_find_all(grid, "O")
    for x, y in locations:
        total += (x * 1) + (y * 100)
    print(total)

    return total


def push_wide(grid, location, direction):
    x, y = location
    dx, dy = direction
    nx, ny = x + dx, y + dy
    if grid[ny][nx] == ".":
        # Move
        grid[y][x] = "."
        grid[y + dy][x + dx] = "@"
        return (x + dx, y + dy)
    elif grid[ny][nx] == "#":
        # Stop
        return location
    elif grid[ny][nx] in ["[", "]"]:
        # push wide box, and any that they pick up
        que = deque()
        que.append((nx, ny))
        if grid[ny][nx] == "[":
            que.append((nx + 1, ny))
        elif grid[ny][nx] == "]":
            que.append((nx - 1, ny))
        while que:
    else:
        raise ValueError(f"Invalid grid cell: {grid[ny][nx]}")

def star2() -> int:
    data = read_input(test=True)
    grid = []
    instructions = []
    line_count = 0
    for line in data:
        new_line = []
        if line_count < 2:
            for c in line:
                if c == "#":
                    new_line.append("#")
                    new_line.append("#")
                elif c == "O":
                    new_line.append("[")
                    new_line.append("]")
                elif c == ".":
                    new_line.append(".")
                    new_line.append(".")
                else:
                    new_line.append("@")
                    new_line.append(".")
            
            grid.append(new_line)
            if set(line) == {"#"}:
                line_count += 1
        else:
            for char in line:
                instructions.append(char)
    grid = to_grid(grid)
    # grid_print(grid)

    # print(instructions)
    for instr in instructions:
        # grid_print(grid)
        # print(instr)
        location = grid_find(grid, "@")
        # print(location)
        if instr == "<":
            push(grid, location, (-1, 0))
        elif instr == ">":
            push(grid, location, (1, 0))
        elif instr == "^":
            push(grid, location, (0, -1))
        elif instr == "v":
            push(grid, location, (0, 1))

    # grid_print(grid)
    total = 0
    locations = grid_find_all(grid, "[")
    for x, y in locations:
        total += (x * 1) + (y * 100)
    print(total)
    return 0


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
