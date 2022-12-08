import sys


def main():
    trees = [[int(ch) for ch in line.strip()] for line in sys.stdin.readlines()]

    def _visible_north(x, y):
        for i in range(x - 1, -1, -1):
            if trees[i][y] >= trees[x][y]:
                return False
        return True

    def _visible_south(x, y):
        for i in range(x + 1, len(trees)):
            if trees[i][y] >= trees[x][y]:
                return False
        return True

    def _visible_east(x, y):
        for i in range(y + 1, len(trees[x])):
            if trees[x][i] >= trees[x][y]:
                return False
        return True

    def _visible_west(x, y):
        for i in range(y - 1, -1, -1):
            if trees[x][i] >= trees[x][y]:
                return False
        return True

    def _visible(x, y):
        return _visible_north(x, y) or _visible_south(x, y) or _visible_east(x, y) or _visible_west(x, y)

    print(sum([_visible(x, y) for x in range(len(trees)) for y in range(len(trees[x]))]))


if __name__ == "__main__":
    main()
