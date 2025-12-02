from aoc2024.utils.utils import read_input

def star1():
    data = read_input()[0].split()
    data = list(map(int, data))
    total = 0
    
    for _ in range(25):
        new = []
        for i, v in enumerate(data):
            if v == 0:
                new.append(1)
            elif len(str(v)) % 2 == 0:
                right, left = int(str(v)[:len(str(v))//2]), int(str(v)[len(str(v))//2:])
                new.append(right)
                new.append(left)
            else:
                new.append(v * 2024)
        data = new
        total = len(data)
    return total

def star2():
    data = read_input()[0].split()
    data = list(map(int, data))
    total = 0
    
    memo = {}
    stones = {}
    stonesSet = set()
    for i in data:
        stones[i] = stones.get(i, 0) + 1
        stonesSet.add(i)
    for i in range(75):
        # print(i)
        # print(len(data))
        new = {}
        for v in stonesSet:
            if v in memo:
                num = stones[v]
                for i in memo[v]:
                    new[i] = num + new.get(i, 0)
            elif v == 0:
                memo[v] = [1]
                new[1] = stones[v]
            elif len(str(v)) % 2 == 0:
                right, left = int(str(v)[:len(str(v))//2]), int(str(v)[len(str(v))//2:])
                memo[v] = [right, left]
                new[right] = new.get(right, 0) + stones[v]
                new[left] = new.get(left, 0) + stones[v]
            else:
                memo[v] = [v * 2024]
                new[v * 2024] = new.get(v * 2024, 0) + stones[v]
        stones = new
        stonesSet = set(stones.keys())
    m = 0
    for v in stones.values():
        m = max(m, v)
        total += v
        
    print(m)
    return total

if __name__ == '__main__':
    print(star1())
    print(star2())