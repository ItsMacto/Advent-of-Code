from aoc2024.utils.utils import read_input, to_grid, grid_find_all, grid_get

def star1():
    data = read_input()
    data = to_grid(data, toInt=True)
    total = 0
    
    trailHeads = grid_find_all(data, 0)
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(x, y, found):
        if grid_get(data, x, y) == 9:
            if (x,y) not in found:
                found.add((x,y))
        next = grid_get(data, x, y) + 1
        
        for xx, yy in direction:
            if next == grid_get(data, x+xx, y+yy):
                dfs(x+xx, y+yy, found)        

    for x, y in trailHeads:
        found = set()
        dfs(x,y,found)
        total += len(found)
        
    return total

def star2():
    data = read_input()
    data = to_grid(data, toInt=True)
    total = 0
    
    trailHeads = grid_find_all(data, 0)
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(x, y, found = 0):
        if grid_get(data, x, y) == 9:
            # print("here")
            return 1
        count = 0
        next = grid_get(data, x, y) + 1
        
        for xx, yy in direction:
            if next == grid_get(data, x+xx, y+yy):
                count += dfs(x+xx, y+yy, found)       
                
        return count 

    for x, y in trailHeads:

        total += dfs(x,y)
    return total

if __name__ == '__main__':
    print(star1())
    print(star2())
