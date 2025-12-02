from aoc2024.utils.utils import read_input

def isSafe(report):
    safe = True
    if report[0] < report[1]:
        for i in range(1, len(report)):
            diff = report[i] - report[i-1]
            if diff > 3 or diff < 1:
                safe = False
                break
    else:
        for i in range(1, len(report)):
            diff = report[i-1] - report[i]
            if diff > 3 or diff < 1:
                safe = False
                break
    return safe

def star1():
    data = read_input()

    data = [list(map(int, x.split())) for x in data]
    total = 0

    for report in data:
        # print(report)
        safe = True
        if report[0] < report[1]:
            for i in range(1, len(report)):
                diff = report[i] - report[i-1]
                if diff > 3 or diff < 1:
                    safe = False
                    break
        else:
            for i in range(1, len(report)):
                diff = report[i-1] - report[i]
                if diff > 3 or diff < 1:
                    safe = False
                    break
        if safe:
            # print('safe')
            total += 1
        
    return total

# 5 2 6 7 8    
# 5 2 6 1 0
def star2():
    data = read_input()

    data = [list(map(int, x.split())) for x in data]
    total = 0
    
    for report in data:
        safe = False
        for i in range(len(report)):
            newReport = report[0:i] + report[i+1:]
            if isSafe(newReport):
                safe = True
                break
        if safe:
            total += 1
            
    return total

    

if __name__ == '__main__':
    print(star1())
    print(star2())    
    