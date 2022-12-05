import string
import sys


def _grouped(iterable, n):
    return zip(*[iter(iterable)] * n)


def _common_item_type(a, b, c):
    return set(a).intersection(set(b)).intersection(set(c)).pop()


def _priority(ch):
    return (string.ascii_lowercase + string.ascii_uppercase).index(ch) + 1


def main():
    lines = [line.strip() for line in sys.stdin.readlines()]
    print(sum([_priority(_common_item_type(*sacks)) for sacks in _grouped(lines, 3)]))


if __name__ == "__main__":
    main()
