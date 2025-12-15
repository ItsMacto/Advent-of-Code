from aoc2025.utils.utils import read_input


def star1() -> int:
    # data = read_input(test=True)
    data = read_input()
    def parse_first_n_shapes(lines: list[str], n: int = 6) -> list[list[str]]:
        shapes: list[list[str]] = []
        cur: list[str] = []
        reading_shape = False

        for raw in lines:
            line = raw.strip()
            if len(shapes) == n:
                break
            if line == "":
                continue

            if line.endswith(":") and line[:-1].isdigit():
                if cur:
                    shapes.append(cur)
                    cur = []
                reading_shape = True
                continue

            if reading_shape and set(line) <= {".", "#"}:
                cur.append(line)

        if cur and len(shapes) < n:
            shapes.append(cur)

        return shapes
    shapes = parse_first_n_shapes(data) # type : ignore
    shapes_sizes = [sum(row.count("#") for row in shape) for shape in shapes]
    print(shapes_sizes)
    
    can_fit_count = 0
    
    for line in data[30:]:
        size, *counts = line.split()
        x, y = map(int, size.strip(":").split("x"))
        size_area = x * y
        min_area = 0
        for i, count in enumerate(counts):
            count_int = int(count)
            shape_area = shapes_sizes[i]
            min_area += (count_int * shape_area)
        if min_area <= size_area:
            can_fit_count += 1
            
    
    return can_fit_count


def star2() -> int:
    data = read_input(test=True)
    # TODO: Implement star 2 solution
    return 0


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
