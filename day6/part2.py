import sys


def main():
    chs = sys.stdin.read()
    for i in range(0, len(chs) - 14):
        if sorted(set(chs[i:i + 14])) == sorted(chs[i:i + 14]):
            print(i + 14)
            break


if __name__ == "__main__":
    main()
