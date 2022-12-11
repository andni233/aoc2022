import sys
import functools
import math
from dataclasses import dataclass
from typing import Callable


@dataclass
class Monkey:
    items: list[int]
    operation: Callable[[int], int]
    test: Callable[[int], bool]
    test_true: int
    test_false: int
    inspected_items: int = 0


def _grouped(iterable, n):
    return zip(*[iter(iterable)] * n)


def _eval_op(op, old):
    return eval(op)


def _test(v, d):
    return d % v == 0


def main():
    monkeys = list()

    for data in _grouped([line.strip() for line in sys.stdin.readlines() if line != "\n"], 6):
        items = [int(d) for d in data[1].split(" ", maxsplit=2)[-1].split(", ")]
        operation = functools.partial(_eval_op, compile(data[2].split(" ", maxsplit=3)[-1], "string", "eval"))
        test = functools.partial(_test, int(data[3].split(" ")[-1]))
        test_true = int(data[4].split(" ")[-1])
        test_false = int(data[5].split(" ")[-1])
        monkeys.append(Monkey(items, operation, test, test_true, test_false))

    def _round():
        for monkey in monkeys:
            for item in monkey.items[::]:
                monkey.items.pop(0)
                monkey.inspected_items += 1
                item = monkey.operation(item) // 3
                if monkey.test(item):
                    monkeys[monkey.test_true].items.append(item)
                else:
                    monkeys[monkey.test_false].items.append(item)

    for _ in range(20):
        _round()

    print(math.prod(sorted([monkey.inspected_items for monkey in monkeys], reverse=True)[:2]))


if __name__ == "__main__":
    main()
