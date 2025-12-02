from aoc2024.utils.utils import read_input
import re
# Time to learn regex for the first time 🙃

def star1():

    data = read_input(splitLines=False)
    # print(data)
    pattern = r"mul\((\d{1,3},\d{1,3})\)"
    match = re.findall(pattern, data)
    # print(match)
    total = 0
    for i in match:
        a, b = i.split(',')
        total += int(a) * int(b)
        
    return total

    
def star2():
    data = read_input(splitLines=False)
    
    # split all the do
    split = data.split('do()')
    strings = []
    
    # that the first split at dont
    for i in split:
        split2 = i.split('don\'t()')
        strings.append(split2[0])
    
    pattern = r"mul\((\d{1,3},\d{1,3})\)"
    match = []
    
    # find all the matches
    for i in strings:
        match += re.findall(pattern, i)
    
    # and get total
    total = 0
    for i in match:
        a, b = i.split(',')
        total += int(a) * int(b)
    return total
    

if __name__ == '__main__':
    print(star1())
    print(star2())
    
    