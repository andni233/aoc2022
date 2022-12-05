import sys


def main():
    m = 0
    c = 0
    for d in [line.strip() for line in sys.stdin.readlines()]:
        if d:
            c += int(d)
        else:
            if c > m:
                m = c
            c = 0
    print(m)


if __name__ == "__main__":
    main()
