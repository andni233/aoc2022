import sys


def main():
    lines = []
    for line in sys.stdin.readlines():
        lines.append(line.replace(": ", " = ").strip())

    while True:
        for line in lines:
            try:
                exec(line, globals(), globals())
            except:
                pass
        try:
            if root:
                break
        except:
            pass

    print(int(root))


if __name__ == "__main__":
    main()
