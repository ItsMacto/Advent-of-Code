from aoc2025.utils.utils import read_input


def star1() -> int:
    data = read_input()
    total = 0
    a, b, p, =  (0,0), (0,0), (0,0)
    # 3 to push a, 1 to push b
    for i, line in enumerate(data):
        if i % 4 == 0:
            x = int(line[line.index(("+")) + 1 : line.index(",")])
            y = int(line[line.index(",") + 3 :])
            a = (x, y)
        elif i % 4 == 1:
            x = int(line[line.index(("+")) + 1 : line.index(",")])
            y = int(line[line.index(",") + 3 :])
            b = (x, y)
        elif i % 4 == 2:
            x = int(line[line.index(("=")) + 1 : line.index(",")])
            y = int(line[line.index(",") + 4 :])
            p = (x, y)
            
            ax, ay = a
            bx, by = b
            px, py = p

            best_cost = None

            for a_presses in range(101):
                for b_presses in range(101):
                    if (
                        ax * a_presses + bx * b_presses == px
                        and ay * a_presses + by * b_presses == py
                    ):
                        cost = 3 * a_presses + b_presses
                        if best_cost is None or cost < best_cost:
                            best_cost = cost

            if best_cost is not None:
                total += best_cost
            

    print(total)
            
    return total


OFFSET = 10_000_000_000_000

# I did not know how to solve this on and forgot about cramer's rule. I had to look it up. 
def star2() -> int:
    data = read_input()
    
    total = 0
    a, b = (0, 0), (0, 0)

    for i, line in enumerate(data):
        if i % 4 == 0:
            # Button A
            x = int(line[line.index("+") + 1 : line.index(",")])
            y = int(line[line.index(",") + 3 :])
            a = (x, y)
        elif i % 4 == 1:
            # Button B
            x = int(line[line.index("+") + 1 : line.index(",")])
            y = int(line[line.index(",") + 3 :])
            b = (x, y)
        elif i % 4 == 2:
            # Prize
            x = int(line[line.index("=") + 1 : line.index(",")])
            y = int(line[line.index(",") + 4 :])
            px = x + OFFSET
            py = y + OFFSET

            ax, ay = a
            bx, by = b

            det = ax * by - ay * bx
            if det == 0:
                # Parallel / dependent - either no solution or infinite; here we can just skip
                continue

            # (ax*by - ay*bx) * A = px*by - py*bx
            A_num = px * by - py * bx
            # (bx*ay - by*ax) * B = px*ay - py*ax -> note bx*ay - by*ax = -det
            B_num = ax * py - ay * px  # equivalent to -(px*ay - py*ax)

            if A_num % det != 0 or B_num % det != 0:
                # Not integer solutions
                continue

            A = A_num // det
            B = B_num // det

            if A < 0 or B < 0:
                # Negative presses don't make sense
                continue

            total += 3 * A + B

    print(total)
    return total

if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
