from aoc2025.utils.utils import read_input


def star1() -> int:
    data = read_input(split=False)
    seen = {(0, 0)}
    x, y = 0, 0
    for v in data:
        match v:
            case "<":
                x -= 1
            case ">":
                x += 1
            case "v":
                y -= 1
            case "^":
                y += 1
        seen.add((x, y))
    return len(seen)


def star2() -> int:
    data = read_input(split=False)
    seen = {(0, 0)}
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    is_Santa_turn = True
    def new_loc(x, y, v):
        match v:
            case "<":
                x -= 1
            case ">":
                x += 1
            case "v":
                y -= 1
            case "^":
                y += 1
        return x, y

    for v in data:
        if is_Santa_turn:
            x1, y1 = new_loc(x1, y1, v)
            seen.add((x1, y1))
        else:
            x2, y2 = new_loc(x2, y2, v)
            seen.add((x2, y2))
        is_Santa_turn = not is_Santa_turn

    return len(seen)


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
