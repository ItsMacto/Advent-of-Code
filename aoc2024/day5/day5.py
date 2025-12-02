from aoc2024.utils.utils import read_input

def star1():
    data = read_input(splitLines=False, fileName="input.txt")
    data = data.split("\n\n")
    ordering = data[0].split("\n")
    pages = data[1].split("\n")
    
    total = 0
    
    for update in pages:
        isValid = True
        update = update.split(",")
        updateSet = set(update)
        for rule in ordering:
            first, second = rule.split("|")
            if first in updateSet and second in updateSet:
                for n in update:
                    if n == first:
                        break
                    if n == second:
                        isValid = False
                        break
            if not isValid:
                break
        if isValid:
            total += int(update[len(update)//2])
            
    return total

def validOrdering(ordering, update):
    updateSet = set(update)
    isValid = True
    for rule in ordering:
        first, second = rule.split("|")
        if first in updateSet and second in updateSet:
            for n in update:
                if n == first:
                    break
                if n == second:
                    isValid = False
                    break
        if not isValid:
            break
    return isValid
    
def star2():
    data = read_input(splitLines=False, fileName="input.txt")
    data = data.split("\n\n")
    ordering = data[0].split("\n")
    pages = data[1].split("\n")
    
    total = 0
    wrongPages = []
    for update in pages:
        isValid = True
        update = update.split(",")
        updateSet = set(update)
        for rule in ordering:
            first, second = rule.split("|")
            if first in updateSet and second in updateSet:
                for n in update:
                    if n == first:
                        break
                    if n == second:
                        isValid = False
                        break
            if not isValid:
                wrongPages.append(update)
                break
            
    for update in wrongPages:
        # update = update.split(",")
        updateSet = set(update)
        isValid = False
        while not isValid:
            for rule in ordering:
                first, second = rule.split("|")
                if first in updateSet and second in updateSet:
                    for n in update:
                        if n == first:
                            break
                        if n == second:
                            i = update.index(first)
                            update.pop(i)
                            update.insert(update.index(second), first)
                            # print(update)
                            break
            isValid = validOrdering(ordering, update)
            if isValid:
                total += int(update[len(update)//2])
        # print(update)
        
                        
    return total

        
        
    return
    

if __name__ == '__main__':
    print(star1())
    print(star2())
    
    