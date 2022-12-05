import sys
import re
from collections import defaultdict


def main():
    stacks = defaultdict(list)

    for line in [line.strip("\n") for line in sys.stdin.readlines()]:
        if "[" in line:
            for i, ch in enumerate(line[1::4], start=1):
                if ch != " ":
                    stacks[i].append(ch)
        elif match := re.match(r"move (\d+) from (\d+) to (\d+)", line):
            count, src, dst = map(int, match.groups())
            for _ in range(count):
                stacks[dst].insert(0, stacks[src].pop(0))

    print("".join(stacks[key].pop(0) for key in sorted(stacks.keys())))


if __name__ == "__main__":
    main()
