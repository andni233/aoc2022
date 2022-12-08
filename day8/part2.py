import sys


def main():
    trees = [[int(ch) for ch in line.strip()] for line in sys.stdin.readlines()]

    def _score_north(x, y):
        score = 0
        for i in range(x - 1, -1, -1):
            score += 1
            if trees[i][y] >= trees[x][y]:
                break
        return score

    def _score_south(x, y):
        score = 0
        for i in range(x + 1, len(trees)):
            score += 1
            if trees[i][y] >= trees[x][y]:
                break
        return score

    def _score_east(x, y):
        score = 0
        for i in range(y + 1, len(trees[x])):
            score += 1
            if trees[x][i] >= trees[x][y]:
                break
        return score

    def _score_west(x, y):
        score = 0
        for i in range(y - 1, -1, -1):
            score += 1
            if trees[x][i] >= trees[x][y]:
                break
        return score

    def _score(x, y):
        return _score_north(x, y) * _score_south(x, y) * _score_east(x, y) * _score_west(x, y)

    print(max([_score(x, y) for x in range(len(trees)) for y in range(len(trees[x]))]))


if __name__ == "__main__":
    main()
