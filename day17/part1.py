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
    winds = itertools.cycle([-1 if w == "<" else 1 for w in sys.stdin.read().strip()])
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
    while fallen_rocks != 2022:
        shape.move(next(winds), 0, occupied_positions)
        if shape.move(0, -1, occupied_positions):
            occupied_positions = occupied_positions.union(shape.positions)
            mh = max([y for _, y in occupied_positions]) + 4
            shape = next(shapes)()
            fallen_rocks += 1

    print(max([y for _, y in occupied_positions]) + 1)


if __name__ == "__main__":
    main()
