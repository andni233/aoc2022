import sys
import itertools
from dataclasses import dataclass


@dataclass
class Shape:
    positions: set[tuple[int, int]]

    def move(self, dx, dy, occupied_positions):
        new_positions = {(x + dx, y + dy) for x, y in self.positions}
        if any({x < 0 or x > 6 for x, _ in new_positions}):
            return False
        if any({(x, y) in occupied_positions for x, y in new_positions}):
            return True
        self.positions = new_positions
        return False


def main():
    input_data = sys.stdin.read().strip()
    winds = itertools.cycle([-1 if w == "<" else 1 for w in input_data])
    occupied_positions = set([(0, -1), (1, -1), (2, -1), (3, -1), (4, -1), (5, -1), (6, -1)])
    mh = 3  # max height
    shapes = itertools.cycle([
        lambda: Shape([(2, mh), (3, mh), (4, mh), (5, mh)]),
        lambda: Shape([(3, mh), (2, mh + 1), (3, mh + 1), (4, mh + 1), (3, mh + 2)]),
        lambda: Shape([(2, mh), (3, mh), (4, mh), (4, mh + 1), (4, mh + 2)]),
        lambda: Shape([(2, mh), (2, mh + 1), (2, mh + 2), (2, mh + 3)]),
        lambda: Shape([(2, mh), (3, mh), (2, mh + 1), (3, mh + 1)]),
    ])
    shape: Shape = next(shapes)()

    fallen_rocks = 0
    cache = {}
    shape_cycle = 0
    wind_cycle = 0
    cycle = None

    def _height():
        return max([y for _, y in occupied_positions])

    while fallen_rocks != 1000000000000:
        if cycle and cycle[1] and (1000000000000 - fallen_rocks) > cycle[1]:
            cycle_count = (1000000000000 - fallen_rocks) // cycle[1]
            fallen_rocks += cycle_count * cycle[1]
            mh += (cycle_count * cycle[0]) + 4
            occupied_positions = {(x, y + cycle_count * cycle[0]) for x, y in occupied_positions}
            shape = next(shapes)()
            continue

        shape.move(next(winds), 0, occupied_positions)
        wind_cycle = (wind_cycle + 1) % len(input_data)

        if shape.move(0, -1, occupied_positions):
            occupied_positions = occupied_positions.union(shape.positions)
            mh = max([y for _, y in occupied_positions]) + 4
            fallen_rocks += 1

            shape = next(shapes)()
            shape_cycle = (shape_cycle + 1) % 5

        board_cycle = ""
        for x in range(0, 7):
            for y in range(mh, 0, -1):
                if (x, y) in occupied_positions:
                    board_cycle += f"{mh - y},"
                    break

        cache_key = f"{wind_cycle}|{shape_cycle}|{board_cycle}"
        if cache_key in cache:
            cycle = (_height() - cache[cache_key][0], fallen_rocks - cache[cache_key][1])
        cache[cache_key] = (_height(), fallen_rocks)

    print(_height())


if __name__ == "__main__":
    main()
