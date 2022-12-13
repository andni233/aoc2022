import sys
import functools


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


def main():
    key = 1
    packets = [eval(packet.strip()) for packet in sys.stdin.readlines() if packet != "\n"]
    for i, packet in enumerate(sorted(packets + [[[2]], [[6]]], key=functools.cmp_to_key(_compare)), start=1):
        if packet == [[2]] or packet == [[6]]:
            key *= i
    print(key)


if __name__ == "__main__":
    main()
