import string
import sys


def _common_item_type(line):
    return set(line[(len(line) // 2):]).intersection(set(line[:(len(line) // 2)])).pop()


def _priority(ch):
    return (string.ascii_lowercase + string.ascii_uppercase).index(ch) + 1


def main():
    print(sum([_priority(_common_item_type(line.strip())) for line in sys.stdin.readlines()]))


if __name__ == "__main__":
    main()
