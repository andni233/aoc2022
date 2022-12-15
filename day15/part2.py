import sys
import re


def taxi_distance(sensor, beacon):
    return abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])


def main():
    grid = list()

    m = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    for x0, y0, x1, y1 in [map(int, re.match(m, line).groups()) for line in sys.stdin.readlines()]:
        grid.append(((x0, y0), (x1, y1)))

    for y in range(4000000):
        ranges = []
        for sensor, beacon in grid:
            distance = taxi_distance(sensor, beacon)

            dy = abs(sensor[1] - y)
            if dy <= distance:
                dx = distance - dy
                ranges.append((sensor[0] - dx, sensor[0] + dx))

        ranges = sorted(ranges)
        combined = [ranges[0]]
        for r in ranges[1:]:
            if combined[-1][1] < r[0]:
                combined.append(r)
            else:
                combined[-1] = (combined[-1][0], max(combined[-1][1], r[1]))

        if len(combined) > 1 or (combined[0][0] > 0 or combined[0][1] < 4000000):
            if len(combined) == 1:
                x = 0 if combined[0][0] > 0 else 4000000
            else:
                x = combined[0][1] + 1
            print(x * 4000000 + y)
            break


if __name__ == "__main__":
    main()
