import sys

def _mix(ds):
    mixed: list = ds[::]
    for i in range(len(mixed)):
        for j, (order, d) in enumerate(mixed):
            if order == i:
                if d == 0:
                    break
                q = mixed.pop(j)
                mixed.insert((j + d) % (len(ds) - 1), q)
                break
    return mixed


def main():
    ds = [(order, int(line.strip())) for order, line in enumerate(sys.stdin.readlines())]
    ds = _mix(ds)
    for i, (_, d) in enumerate(ds):
        if d == 0:
            print(sum([ds[(i + 1000) % len(ds)][1], ds[(i + 2000) % len(ds)][1], ds[(i + 3000) % len(ds)][1]]))


if __name__ == "__main__":
    main()
