import sys
import re


def taxi_distance(sensor, beacon):
    return abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])


def main():
    grid = list()

    m = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    for x0, y0, x1, y1 in [map(int, re.match(m, line).groups()) for line in sys.stdin.readlines()]:
        grid.append(((x0, y0), (x1, y1)))

    ranges = []
    for sensor, beacon in grid:
        distance = taxi_distance(sensor, beacon)

        dy = abs(sensor[1] - 2000000)
        if dy <= distance:
            dx = distance - dy
            ranges.append((sensor[0] - dx, sensor[0] + dx))

    ranges = sorted(ranges)
    combined = [ranges[0]]
    for range in ranges[1:]:
        if combined[-1][1] < range[0]:
            combined.append(range)
        else:
            combined[-1] = (combined[-1][0], max(combined[-1][1], range[1]))

    positions_no_beacon = 0
    for range in combined:
        positions_no_beacon += (range[1] - range[0])

    print(positions_no_beacon)


if __name__ == "__main__":
    main()
