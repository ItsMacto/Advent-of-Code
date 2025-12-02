from aoc2024.utils.utils import read_input, grid_find_all, grid_get, to_grid
from math import gcd

def star1():
    data = read_input()
    # data = read_input("test.txt")
    data = to_grid(data)
    total = set()
    # print(data)
    antennaSet = set(item for sublist in data for item in sublist)
    antennaSet.remove(".")
    antennasDict = {}
    
    for antenna in antennaSet:
        antennasDict[antenna] = grid_find_all(data, antenna)
        
    for antenna in antennaSet:
        if len(antennasDict[antenna]) > 1:
            for i in range(len(antennasDict[antenna])):
                for j in range(i+1, len(antennasDict[antenna])):
                    x1, y1 = antennasDict[antenna][i]
                    x2, y2 = antennasDict[antenna][j]
                    x3, y3 = 2*x1 - x2, 2*y1 - y2
                    x4, y4 = 2*x2 - x1, 2*y2 - y1
                    if grid_get(data, x3, y3, default=None):
                        total.add((x3, y3))
                    if grid_get(data, x4, y4, default=None):
                        total.add((x4, y4))    
    
    return len(total)

def star2():
    data = read_input()
    # data = read_input("test.txt")
    data = to_grid(data)
    total = set()
    # print(data)
    antennaSet = set(item for sublist in data for item in sublist)
    antennaSet.remove(".")
    # antennaSet.remove("#")
    antennasDict = {}
    
    for antenna in antennaSet:
        antennasDict[antenna] = grid_find_all(data, antenna)
        
    for antenna in antennaSet:
        if len(antennasDict[antenna]) > 1:
            for i in range(len(antennasDict[antenna])):
                for j in range(i+1, len(antennasDict[antenna])):
                    x1, y1 = antennasDict[antenna][i]
                    x2, y2 = antennasDict[antenna][j]
                    total.add((x1, y1))
                    total.add((x2, y2))
                    
                    dx, dy = x2 - x1, y2 - y1
                    
                    g = gcd(dx, dy)
                    
                    dx //= g
                    dy //= g
                    
                    x, y = x1 + dx, y1 + dy
                    while grid_get(data, x, y, default=None):
                        total.add((x, y))
                        x += dx
                        y += dy
                        
                    x, y = x1 - dx, y1 - dy
                    while grid_get(data, x, y, default=None):
                        total.add((x, y))
                        x -= dx
                        y -= dy
                    
                            
    # print(total)
    
    return len(total)

if __name__ == '__main__':
    print(star1())
    print(star2())
