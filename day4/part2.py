import sys


def _parse_range(it):
    start, end = (int(x) for x in it.split("-"))
    return set(range(start, end + 1))


def main():
    count = 0
    for a, b in [tuple(pair.split(",")) for pair in sys.stdin.read().split()]:
        a, b = _parse_range(a), _parse_range(b)
        if a.intersection(b):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
