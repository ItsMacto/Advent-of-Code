from aoc2025.utils.utils import read_input
from collections import deque
import z3

# import heapq
# from functools import lru_cache


def star1() -> int:
    def solve(target: list[bool], current: list[bool], buttons: list[list[int]]) -> int:

        initial_state = tuple(current)
        target_state = tuple(target)
        queue = deque([(initial_state, 0)])
        visited = {initial_state: 0}

        while queue:
            state, steps = queue.popleft()
            if state == target_state:
                return steps

            for button in buttons:
                new_state = list(state)
                for index in button:
                    new_state[index] = not new_state[index]
                new_state_tuple = tuple(new_state)
                if new_state_tuple not in visited or visited[new_state_tuple] > steps + 1:
                    visited[new_state_tuple] = steps + 1
                    queue.append((new_state_tuple, steps + 1))

        return -1 
    
    data = read_input()
    indicators = []
    buttons_list = []
    for line in data:
        elements = line.split()
        indicator = [True if c == "#" else False for c in elements[0][1:-1]]
        buttons = [list(map(int, x[1:-1].split(","))) for x in elements[1:-1]]
        indicators.append(indicator)
        buttons_list.append(buttons)
        
    total_steps = 0
    for indicator, buttons in zip(indicators, buttons_list):
        steps = solve(indicator, [False] * len(indicator), buttons)
        total_steps += steps
        # print(f"Indicator: {indicator}, Steps: {steps}")
    
    return total_steps


# I used ai here. Dint really know z3
def star2() -> int:
    # data = read_input(test=True)
    data = read_input()
    jolts = []
    buttons_list = []
    for i, line in enumerate(data):
        # print(i)
        elements = line.split()
        buttons = [list(map(int, x[1:-1].split(","))) for x in elements[1:-1]]
        jolt = [int(x) for x in elements[-1][1:-1].split(",")]
        buttons_list.append(buttons)
        jolts.append(jolt)

    total_steps = 0
    for line_idx, (jolt, buttons) in enumerate(zip(jolts, buttons_list)):
        opt = z3.Optimize()

        # btn_k = how many times we press button k
        button_vars = [z3.Int(f"btn_{line_idx}_{k}") for k in range(len(buttons))]

        # Non-negative presses
        for var in button_vars:
            opt.add(var >= 0)

        # For each jolt index i:
        #   sum over all buttons that affect i of presses = jolt[i]
        for i in range(len(jolt)):
            terms = []
            for j, btn in enumerate(buttons):
                if i in btn:
                    terms.append(button_vars[j])

            if terms:
                expr = z3.Sum(terms)
            else:
                # No button ever touches this index; so it can only be 0
                expr = z3.IntVal(0)

            opt.add(expr == jolt[i])

        # Minimize total number of button presses
        total_presses = z3.Sum(button_vars)
        opt.minimize(total_presses)

        if opt.check() != z3.sat:
            raise RuntimeError(f"No solution for line {line_idx}")

        model = opt.model()
        total_steps += model.eval(total_presses).as_long()
    
    
    return total_steps

'''
A* and greedy wont even work for this sadly
'''
# def star2() -> int:
#     # @lru_cache(None)
#     def distance(a: tuple[int, ...], b: tuple[int, ...]) -> int:
#         return sum(abs(x - y) for x, y in zip(a, b))
#     # @lru_cache(None)
#     def distance2(a: list[int], b: list[int]) -> int:
#         return max(y - x for x, y in zip(a, b))
    

#     def solve(target: list[int], current: list[int], buttons: list[list[int]]) -> int:
#         initial_state = tuple(current)
#         target_state = tuple(target)
#         initial_distance = distance2(initial_state, target_state)
#         heap = [(initial_distance, 0, initial_state)]
#         visited = {initial_state: 0}
        
    

#         while heap:
#             d, steps, state = heapq.heappop(heap)
#             if state in visited and visited[state] < steps:
#                 continue
#             print(d, state)
#             if state == target_state:
#                 return steps

#             for button in buttons:
#                 new_state = list(state)
#                 valid = True
#                 for x in button:
#                     # print(button, x, new_state)
#                     new_state[x] += 1
#                     if new_state[x] > target[x]:
#                         valid = False
#                         break
#                 if not valid:
#                     continue
#                 new_state_tuple = tuple(new_state)
#                 if new_state_tuple not in visited or visited[new_state_tuple] > steps + 1:
#                     visited[new_state_tuple] = steps + 1
#                     new_distance = distance2(new_state_tuple, target_state)
#                     # heapq.heappush(heap, (new_distance, steps + 1, new_state_tuple))
#                     heapq.heappush(heap, (new_distance + steps + 1, steps + 1, new_state_tuple))
#         return -1 
#     # data = read_input(test=True)
#     data = read_input()
#     jolts = []
#     buttons_list = []
#     for i, line in enumerate(data):
#         print(i)
#         elements = line.split()
#         buttons = [list(map(int, x[1:-1].split(","))) for x in elements[1:-1]]
#         jolt = [int(x) for x in elements[-1][1:-1].split(",")]
#         buttons_list.append(buttons)
#         jolts.append(jolt)
    
#     total_steps = 0
#     for jolt, buttons in zip(jolts, buttons_list):
#         steps = solve(jolt, [0] * len(jolt), buttons)
#         total_steps += steps
    
#     return total_steps


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
