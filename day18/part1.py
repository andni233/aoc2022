import sys


def main():
    coords = [tuple(int(x) for x in line.strip().split(",")) for line in sys.stdin.readlines()]
    visible_sides = 0
    for x, y, z in coords:
        for side in [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]:
            if side not in coords:
                visible_sides += 1
    print(visible_sides)


if __name__ == "__main__":
    main()
