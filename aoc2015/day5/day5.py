from aoc2025.utils.utils import read_input
from collections import defaultdict

def star1() -> int:
    cant_have = ["ab", "cd", "pq", "xy"]
    data = read_input()
    total = 0
    for line in data:
        is_cant_have = False
        for seq in cant_have:
            if seq in line:
                is_cant_have = True
                break
        if is_cant_have:
            continue
        
        vowel_count = sum(1 for c in line if c in "aeiou")
        if vowel_count < 3:
            continue
        has_double = any(line[i] == line[i+1] for i in range(len(line)-1))
        if not has_double:
            continue
        total += 1
    return total
                
                
        
def star2() -> int:
    data = read_input()
    total = 0
    for line in data:
        pairs = defaultdict(int)
        has_pair = False
        for i in range(len(line)-1):
            pair = line[i:i+2]
            pairs[pair] += 1
            if pairs[pair] > 1:
                first_index = line.find(pair)
                second_index = line.find(pair, first_index + 2)
                if second_index != -1:
                    has_pair = True
                    break
        if not has_pair:
            continue
        
        has_repeat = any(line[i] == line[i+2] for i in range(len(line)-2))
        if not has_repeat:
            continue
        total += 1
    return total
        

if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
