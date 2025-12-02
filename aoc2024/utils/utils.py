import os
import inspect

def read_input(fileName="input.txt", splitLines=True):
    # Get the path of the calling script
    caller_frame = inspect.stack()[1]
    caller_file = caller_frame.filename
    caller_dir = os.path.dirname(caller_file)

    # Resolve the path to the input file relative to the calling script
    file_path = os.path.join(caller_dir, fileName)
    
    # Read the file
    with open(file_path) as f:
        if splitLines:
            return f.read().splitlines()
        else:
            return f.read()
        
def to_grid(data, toInt=False):
    if toInt:
        return [list(map(int, row)) for row in data]
    else:
        return [list(row) for row in data]

def grid_rotate(grid, times=1):
    for _ in range(times):
        grid = list(zip(*grid[::-1]))
    return grid

def grid_get(grid, x, y, default="."):
    if x < 0 or y < 0:
        return default
    try:
        return grid[y][x]
    except IndexError:
        return default
    
def grid_find(grid, target):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == target:
                return (x, y)
    return None

def grid_find_all(grid, target):
    results = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == target:
                results.append((x, y))
    return results

def grid_print(grid):
    for row in grid:
        print("".join(row))