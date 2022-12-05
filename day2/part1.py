import sys


_move_to_score = {
    ("A", "Z"): 3 + 0,
    ("A", "X"): 1 + 3,
    ("A", "Y"): 2 + 6,
    ("B", "Z"): 3 + 6,
    ("B", "X"): 1 + 0,
    ("B", "Y"): 2 + 3,
    ("C", "Z"): 3 + 3,
    ("C", "X"): 1 + 6,
    ("C", "Y"): 2 + 0,
}


def main():
    print(sum([_move_to_score[tuple(line.strip().split(" "))] for line in sys.stdin.readlines()]))


if __name__ == "__main__":
    main()
