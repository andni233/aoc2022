import sys


def main():
    chs = sys.stdin.read()
    for i in range(0, len(chs) - 4):
        if sorted(set(chs[i:i + 4])) == sorted(chs[i:i + 4]):
            print(i + 4)
            break


if __name__ == "__main__":
    main()
