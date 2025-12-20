from aoc2025.utils.utils import read_input
import hashlib

def star1() -> int:
    data = read_input(split=False)
    i = 0
    while True:
        test_str = f"{data}{i}".encode()
        hash_result = hashlib.md5(test_str).hexdigest()
        if hash_result.startswith("00000"):
            return i
        i += 1
    
    return -1


def star2() -> int:
    data = read_input(split=False)
    i = 0
    while True:
        test_str = f"{data}{i}".encode()
        hash_result = hashlib.md5(test_str).hexdigest()
        if hash_result.startswith("000000"):
            return i
        i += 1
    return 0


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
