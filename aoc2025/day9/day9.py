from aoc2025.utils.utils import read_input, points_to_grid, grid_print, grid_find, grid_get
from collections import defaultdict


def star1() -> int:
    data = read_input()
    max_area = 0
    
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            ax, ay =  map(int, data[i].split(","))
            bx, by =  map(int, data[j].split(","))
            
            max_area = max((abs(ax - bx) + 1) * (abs(ay - by) + 1), max_area)
    
    return max_area
    
    
def area_fill(grid):
    outside = set()
    start = (0,0)
    if grid_get(grid, start[1], start[0]) != '.':
        assert False, "Starting point is not outside"
    to_visit: list[tuple[int, int]] = [start]
    while to_visit:
        x, y = to_visit.pop()
        if (x, y) in outside:
            continue
        outside.add((x, y))
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if grid_get(grid, ny, nx) == '.':
                to_visit.append((nx, ny))
                
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x, y) not in outside and grid[y][x] == '.':
                grid[y][x] = 'X'
    

def star2() -> int:
    data = read_input()
    # data = read_input(test=True)
    data.append(data[0]) # type: ignore # type : ignore

    all_x = sorted(set(int(line.split(",")[0]) for line in data))
    all_y = sorted(set(int(line.split(",")[1]) for line in data))

    x_to_compressed = {x: 2*i+1 for i, x in enumerate(all_x)}
    y_to_compressed = {y: 2*i+1 for i, y in enumerate(all_y)}

    compressed_data = []
    for line in data:
        x, y = map(int, line.split(","))
        compressed_data.append(f"{x_to_compressed[x]},{y_to_compressed[y]}")

    grid = points_to_grid([(x, y) for x, y in (map(int, line.split(",")) for line in compressed_data)])

    # Add padding to right and bottom
    for row in grid:
        row.append('.')
    grid.append(['.'] * len(grid[0]))

    for i in range(len(compressed_data)-1):
        ax, ay = map(int, compressed_data[i].split(","))
        bx, by = map(int, compressed_data[i+1].split(","))
        if ay == by:
            if ax > bx:
                ax, bx = bx, ax
            for x in range(ax, bx+1):
                if grid[ay][x] != '#':
                    grid[ay][x] = 'X'
        elif ax == bx:
            if ay > by:
                ay, by = by, ay
            for y in range(ay, by+1):
                if grid[y][ax] != '#':
                    grid[y][ax] = 'X'
    # print()
    # grid_print(grid)
    area_fill(grid)
    # print()
    # grid_print(grid)
    max_area = 0

    for i in range(len(data)):
        for j in range(i+1, len(data)):
            ax_orig, ay_orig = map(int, data[i].split(","))
            bx_orig, by_orig = map(int, data[j].split(","))

            ax_comp, ay_comp = map(int, compressed_data[i].split(","))
            bx_comp, by_comp = map(int, compressed_data[j].split(","))

            min_x, max_x = min(ax_comp, bx_comp), max(ax_comp, bx_comp)
            min_y, max_y = min(ay_comp, by_comp), max(ay_comp, by_comp)

            top_ok = all(grid[min_y][x] != '.' for x in range(min_x, max_x + 1))
            bottom_ok = all(grid[max_y][x] != '.' for x in range(min_x, max_x + 1))
            left_ok = all(grid[y][min_x] != '.' for y in range(min_y, max_y + 1))
            right_ok = all(grid[y][max_x] != '.' for y in range(min_y, max_y + 1))
            if top_ok and bottom_ok and left_ok and right_ok:
                max_area = max((abs(ax_orig - bx_orig) + 1) * (abs(ay_orig - by_orig) + 1), max_area)

    return max_area


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
