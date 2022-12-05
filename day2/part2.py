import sys


_move_to_score = {
    ("A", "Z"): 2 + 6,
    ("A", "X"): 3 + 0,
    ("A", "Y"): 1 + 3,
    ("B", "Z"): 3 + 6,
    ("B", "X"): 1 + 0,
    ("B", "Y"): 2 + 3,
    ("C", "Z"): 1 + 6,
    ("C", "X"): 2 + 0,
    ("C", "Y"): 3 + 3,
}


def main():
    print(sum([_move_to_score[tuple(line.strip().split(" "))] for line in sys.stdin.readlines()]))


if __name__ == "__main__":
    main()
