from aoc2025.utils.utils import read_input

class UnionFind:
    def __init__(self, n) -> None:
        self.parent = list(range(n))
        self.rank = [1] * n
        
    def find(self, i) -> int: # type: ignore
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
            
    def union(self, i, j, check_last=False):
        A = self.find(i)
        B = self.find(j)
        if A == B:
            return False
        
        if self.rank[A] < self.rank[B]:
            self.parent[A] = B
            self.rank[B] += self.rank[A]
        elif self.rank[A] > self.rank[B]:
            self.parent[B] = A
            self.rank[A] += self.rank[B]
        else:
            self.parent[B] = A
            self.rank[A] += self.rank[B]
        
        if check_last:
            if max(self.rank[A], self.rank[B]) == len(self.parent):
                return True
            else:
                return False
        return True
    
    def count_groups(self) -> list[int]:
        groups = []
        for i in range(len(self.parent)):
            if i == self.parent[i]:
                groups.append(self.rank[i])
                
        return groups
        

def star1() -> int:
    data = read_input()
    boxes = [list(map(int, line.split(','))) for line in data]
    # print(boxes)
    
    def euclidean_distance(box1, box2):
        return sum((a - b) ** 2 for a, b in zip(box1, box2)) ** 0.5
    
    distances = []
    
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            dist = euclidean_distance(boxes[i], boxes[j])
            distances.append([dist, i, j])
    
    distances.sort()
    
    NUM_TIMES = 1000
    uf = UnionFind(len(data))
    
    for i in range(NUM_TIMES):
        _, A, B = distances[i]
        uf.union(A, B)
        
    groups = uf.count_groups()
    groups.sort(reverse=True)
    
    total = 1
    for i in range(3):
        total *= groups[i]
        
    return total

def star2() -> int:
    data = read_input()
    boxes = [list(map(int, line.split(','))) for line in data]
    # print(boxes)
    
    def euclidean_distance(box1, box2):
        return sum((a - b) ** 2 for a, b in zip(box1, box2)) ** 0.5
    
    distances = []
    
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            dist = euclidean_distance(boxes[i], boxes[j])
            distances.append([dist, i, j])
    
    distances.sort()
    
    uf = UnionFind(len(data))
    
    for i in range(len(distances)):
        _, A, B = distances[i]
        if uf.union(A, B, check_last=True):
            return boxes[A][0] * boxes[B][0]
    
    return 0


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
