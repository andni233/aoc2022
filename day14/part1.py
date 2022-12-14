import sys


def main():
    rocks = set()
    sand = set()
    bound = 0

    for data in [line.strip().split(" -> ") for line in sys.stdin.readlines()]:
        paths = [tuple(int(i) for i in j.split(",")) for j in data]
        for (x0, y0), (x1, y1) in zip(paths, paths[1:]):
            for x in range(min(x0, x1), max(x0, x1) + 1):
                for y in range(min(y0, y1), max(y0, y1) + 1):
                    rocks.add((x, y))
                    bound = max(bound, y)

    def _blocked(x, y):
        return (x, y) in rocks or (x, y) in sand

    def _next_sand_position():
        x, y = 500, 0
        while y <= bound:
            if not _blocked(x, y + 1):
                x, y = x, y + 1
            elif not _blocked(x - 1, y + 1):
                x, y = x - 1, y + 1
            elif not _blocked(x + 1, y + 1):
                x, y = x + 1, y + 1
            else:
                return x, y

    count = 0
    while position := _next_sand_position():
        sand.add(position)
        count += 1

    print(count)


if __name__ == "__main__":
    main()
