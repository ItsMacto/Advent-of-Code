from aoc2025.utils.utils import read_input, to_grid, grid_print, grid_get, grid_find
from collections import deque
from functools import cache

def star1() -> int:
    data = read_input()
    data = to_grid(data)
    start = grid_find(data, 'S')
    # grid_print(data)
    splits = set()
    next = deque()
    next.append(start)
    while next:
        pos = next.popleft()
        next_pos = grid_get(data, pos[1] + 1, pos[0])
        if next_pos and pos not in splits:
            if next_pos == '^':
                splits.add(pos)
                next.append((pos[0] + 1, pos[1] + 1))
                next.append((pos[0] - 1, pos[1] + 1))
            else:
                next.append((pos[0], pos[1] + 1))
    return len(splits)


def star2() -> int:    
    data = read_input()
    data = to_grid(data)
    @cache
    def dfs(pos):
        if not grid_get(data, pos[1], pos[0]):
            return 1
        
        if data[pos[1]][pos[0]] == '^':
            return dfs((pos[0] + 1, pos[1] + 1)) + dfs((pos[0] - 1, pos[1] + 1))
        else:
            return dfs((pos[0], pos[1] + 1))
    start = grid_find(data, 'S')
    result = dfs(start)
    
    return result


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
