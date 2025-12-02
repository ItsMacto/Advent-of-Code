from aoc2024.utils.utils import read_input, grid_find, grid_get, grid_print

def star1():
    data = read_input()
    map = [list(line) for line in data]
    
    direction = (0,1)
    start = grid_find(map,"^")
    map[start[1]][start[0]] = "X"
    # print(start)
    
    total = 1
    while True:
        # print(start, direction)
        # grid_print(map)
        next = (start[0] + direction[0], start[1] + -direction[1])
        val = grid_get(map, next[0], next[1], default=None)
        # print(val)
        if val == ".":
            map[next[1]][next[0]] = "X"
            total += 1
            start = next
        elif val == "X":
            start = next
        elif val == "#":
            # print("hit wall")
            direction = (direction[1], -direction[0])
        else:
            break
    return total

def walkMap(map, past, start, direction):
    grid = map
    if grid_get(grid, start[0], start[1], default=None) != ".":
        return False
    while True:
        next = (start[0] + direction[0], start[1] + -direction[1])
        val = grid_get(grid, next[0], next[1], default=None)
        if val == ".":
            grid[next[1]][next[0]] = "X"
            if next in past:
                if direction in past[next]:
                    print(next, direction)
                    grid_print(grid)
                    return True
            start = next
        elif val == "X":
            start = next
        elif val == "#":
            direction = (direction[1], -direction[0])
        else:
            grid_print(grid)
            return False

def star2():
    data = read_input(fileName="test.txt")
    map = [list(line) for line in data]
    
    direction = (0,1)
    start = grid_find(map,"^")
    current = start
    map[current[1]][current[0]] = "."
    past = {current: set()}
    past[current].add(direction)
    total = 0
    while True:
        next = (current[0] + direction[0], current[1] + -direction[1])
        val = grid_get(map, next[0], next[1], default=None)
        if val == ".":
            # past[next] = past.get(next, []).append(direction)
            past.setdefault(next, set()).add(direction)
            current = next
        elif val == "#":
            direction = (direction[1], -direction[0])
        else:
            break
    # print(past)
    current = start
    direction = (0,1)
    while True:
        
        if current != start and walkMap(map, past, (current[0] + direction[1], current[1] - direction[0]), (direction[1], -direction[0])):
            print(current)
            total += 1
        next = (current[0] + direction[0], current[1] + -direction[1])
        val = grid_get(map, next[0], next[1], default=None)
        
        if val == ".":
            current = next
        elif val == "#":
            direction = (direction[1], -direction[0])
        else:
            break
    
    return total

    
def star2():
    data = read_input(fileName="test.txt")
    map = [list(line) for line in data]
    
    direction = (0, 1)  # Initial direction (up)
    start = grid_find(map, "^")
    current = start
    
    # Remove guard's initial position marker
    map[current[1]][current[0]] = "."
    
    # Dictionary to track visited positions and directions
    past = {current: set()}
    past[current].add(direction)
    
    total = 0
    
    # Function to simulate the guard's movement and determine if a loop forms
    def walk_map_with_obstruction(map, past, start, obstruction_pos, obstruction_dir):
        grid = [row[:] for row in map]  # Clone the map to simulate obstruction
        grid[obstruction_pos[1]][obstruction_pos[0]] = "#"  # Add the obstruction
        current = start
        direction = obstruction_dir
        visited = set()
        
        while True:
            next_pos = (current[0] + direction[0], current[1] - direction[1])
            val = grid_get(grid, next_pos[0], next_pos[1], default=None)
            if val == ".":
                if (next_pos, direction) in visited:
                    return True  # Loop detected
                visited.add((next_pos, direction))
                current = next_pos
            elif val == "#":
                direction = (direction[1], -direction[0])  # Turn right
            else:
                break
        
        return False
    
    # Explore all positions for potential obstructions
    for y in range(len(map)):
        for x in range(len(map[0])):
            if (x, y) != start and map[y][x] == ".":
                if walk_map_with_obstruction(map, past, start, (x, y), direction):
                    total += 1
    
    return total
if __name__ == '__main__':
    print(star1())
    print(star2())
    
    