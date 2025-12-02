from aoc2024.utils.utils import read_input

def star1():
    # data = read_input(fileName="test.txt")
    data = read_input()
    data = [int(digit) for digit in data[0]]
    total = 0
    length = 0 

    for i in range(len(data)):
        length += int(data[i])

    # print(length)
    disk = [0] * length
    
    l, r = 0, len(data) - 1
    lid, rid = 0, len(data) // 2

    i = 0
    left = True
    blanks = 0

    while l <= r:
        if left:
            for _ in range(data[l]):
                disk[i] = lid
                i += 1
            l += 1
            lid += 1
            blanks = data[l]
            left = False
        else:
            for _ in range(blanks):
                if data[r] == 0:
                    r -= 2
                    rid -= 1
                disk[i] = rid
                i += 1
                data[r] -= 1
            l += 1
            left = True
    # print(disk)
    for i, v in enumerate(disk):
        total += v * i
    return total

def star2():
    def get_smallest_index(blankMap, blankKeys, size):
        value = float('inf')
        dict = None
        for key in blankKeys:
            if key >= size:
                if min(blankMap[key]) < value:
                    value = min(blankMap[key])
                    dict = key 
        return value, dict

    data = read_input(fileName="test.txt")
    # data = read_input()
    data = [int(digit) for digit in data[0]]
    total = 0
    length = 0 

    for i in range(len(data)):
        length += int(data[i])

    # print(length)
    disk = [0] * length
    blankMap = {}
    blankKeys = set()
    for i in range(1, len(data), 2):
        blankMap.setdefault(data[i], []).append(i)
        blankKeys.add(data[i])
    
    l, r = 0, len(data) - 1
    lid, rid = 0, len(data) // 2
    left = True
    i = 0
    while l <= r:
        if left:
            for _ in range(data[l]):
                disk[i] = lid
                i += 1
            lid += 1
            l += 1
            l += data[l]
            left = False
        else:
            size = data[r]
            index, dict = get_smallest_index(blankMap, blankKeys, size)
            if dict is not None and index < rid:
                for j in range(data[r]):
                    disk[index + j] = rid
                if dict > size:
                    blankMap[dict].remove(index)
                    if blankMap[dict] == []:
                        blankKeys.remove(dict)
                    blankMap.setdefault(dict - size, []).append(index)
                    blankKeys.add(dict - size)
                else:
                    blankMap[dict].remove(index)
                    if blankMap[dict] == []:
                        blankKeys.remove(dict)
                r -= 2
            l += 1
            left = True
            rid -= 1
    print(disk)
    
    for i, v in enumerate(disk):
        total += v * i
    return total

if __name__ == '__main__':
    print(star1())
    print(star2())
