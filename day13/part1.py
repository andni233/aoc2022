import sys


def _grouped(iterable, n):
    return zip(*[iter(iterable)] * n)


def _compare(left, right):
    match left, right:
        case int(), int():
            return left - right
        case list(), list():
            for a, b in zip(left, right):
                result = _compare(a, b)
                if result:
                    return result
            return len(left) - len(right)
        case int(), list():
            return _compare([left], right)
        case list(), int():
            return _compare(left, [right])


def _in_right_order(left, right):
    return _compare(left, right) < 0


def main():
    sum = 0
    lines = _grouped(sys.stdin.readlines(), 3)
    for i, (left, right) in enumerate([tuple([eval(l.strip()) for l in pair[:-1]]) for pair in lines], start=1):
        if _in_right_order(left, right):
            sum += i
    print(sum)


if __name__ == "__main__":
    main()
