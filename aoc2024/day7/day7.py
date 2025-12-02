from aoc2024.utils.utils import read_input

def star1():
    def dfs(number, index, operation, target):
        if operation == '+':
            number += numbers[index]
        elif operation == '*':
            number *= numbers[index]
        
        index += 1
        if index == len(numbers):
            return False
        # print(number, index, operation, target)
        return dfs(number, index, '+', target) or dfs(number, index, '*', target)
    
    data = read_input()
    total = 0
    for line in data:
        target, numbers = line.split(":")
        target = int(target)
        numbers = list(int(number) for number in numbers.split(" ")[1:])
        if dfs(numbers[0], 1, '+', target) or dfs(numbers[0], 1, '*', target):
            total += target
    return total

def star2():
    def dfs(number, index, operation, target):
        # if index == len(numbers) - 1:
        #     return number == target
        # if target < number:
        #     return False
        
        if operation == '+':
            number += numbers[index]
        elif operation == '*':
            number *= numbers[index]
        elif operation == '||':
            number = int(str(number) + str(numbers[index]))


        index += 1
        if index == len(numbers):
            if number == target:
                return True
            else:
                return False
        return (
            dfs(number, index, '+', target) or 
            dfs(number, index, '*', target) or 
            dfs(number, index, '||', target)
        )
        
    data = read_input()
    # data = read_input(fileName="test.txt")
    total = 0
    for line in data:
        target, numbers = line.split(":")
        target = int(target)
        numbers = list(int(number) for number in numbers.split(" ")[1:])
        if dfs(numbers[0], 1, '+', target) or dfs(numbers[0], 1, '*', target) or dfs(numbers[0], 1, '||', target):
            total += target
            print("Found", target)
    return total

if __name__ == '__main__':
    print(star1())
    print(star2())
