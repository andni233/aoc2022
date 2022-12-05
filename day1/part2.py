import sys


def main():
    elfs = []
    c = 0
    for d in [line.strip() for line in sys.stdin.readlines()]:
        if d:
            c += int(d)
        else:
            elfs.append(c)
            c = 0
    print(sum(sorted(elfs, reverse=True)[:3]))


if __name__ == "__main__":
    main()
