import sys


def main():
    levels = []
    end = None

    for x, line in enumerate(sys.stdin.readlines()):
        levels.append([])
        for y, ch in enumerate(line.strip()):
            if ch == "S":
                ch = "a"
            if ch == "E":
                end = (x, y)
                ch = "z"
            levels[-1].append(ord(ch) - 97)

    def _next(point):
        x, y = point
        steps = []
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            try:
                if levels[x + dx][y + dy] < levels[x][y] or abs(levels[x + dx][y + dy] - levels[x][y]) <= 1:
                    if (x + dx) > 0 and (y + dy > 0):
                        steps.append((x + dx, y + dy))
            except IndexError:
                pass
        return steps

    def _search(start):
        points = [start]
        visited = {start: None}

        while points:
            point = points.pop(0)
            if point == end:
                break
            for step in _next(point):
                if step not in visited:
                    points.append(step)
                    visited[step] = point
        else:
            return None

        point = end
        path = []
        while point != start:
            path.append(point)
            point = visited[point]

        return len(path)

    solutions = [_search((x, y)) for x in range(len(levels)) for y in range(len(levels[x])) if levels[x][y] == 0]
    print(min([solution for solution in solutions if solution is not None]))


if __name__ == "__main__":
    main()
