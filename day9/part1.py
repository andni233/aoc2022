import sys
from dataclasses import dataclass, field


@dataclass
class Tail:
    position: tuple[int, int] = (0, 0)
    visited_positions: set[tuple[int, int]] = field(default_factory=set)

    def adjacent(self, head):
        return abs(head.position[0] - self.position[0]) <= 1 and abs(head.position[1] - self.position[1]) <= 1

    def follow(self, head):
        if not self.adjacent(head):
            x_offset = 1 if self.position[0] < head.position[0] else -1
            y_offset = 1 if self.position[1] < head.position[1] else -1
            if head.position[0] == self.position[0]:
                self.position = (self.position[0], self.position[1] + y_offset)
            elif head.position[1] == self.position[1]:
                self.position = (self.position[0] + x_offset, self.position[1])
            else:
                self.position = (self.position[0] + x_offset, self.position[1] + y_offset)
        self.visited_positions.add(self.position)


@dataclass
class Head:
    tail: Tail
    position: tuple[int, int] = (0, 0)

    def move(self, direction):
        match direction:
            case "U":
                self.position = (self.position[0], self.position[1] + 1)
            case "D":
                self.position = (self.position[0], self.position[1] - 1)
            case "L":
                self.position = (self.position[0] - 1, self.position[1])
            case "R":
                self.position = (self.position[0] + 1, self.position[1])
        self.tail.follow(self)


def main():
    tail = Tail()
    head = Head(tail)

    for direction, x in [line.strip().split() for line in sys.stdin.readlines()]:
        for _ in range(int(x)):
            head.move(direction)

    print(len(tail.visited_positions))


if __name__ == "__main__":
    main()
