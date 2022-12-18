import sys


def main():
    coords = [tuple(int(x) for x in line.strip().split(",")) for line in sys.stdin.readlines()]
    internal_coords = []

    min_x, min_y, min_z = min([x for x, _, _ in coords]), min([y for _, y, _ in coords]), min([z for _, _, z in coords])
    max_x, max_y, max_z = max([x for x, _, _ in coords]), max([y for _, y, _ in coords]), max([z for _, _, z in coords])

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_z, max_z + 1):
                if (x, y, z) not in coords:
                    probes = 0
                    for x_neg in range(min_x, x):
                        if (x_neg, y, z) in coords:
                            probes += 1
                            break
                    for x_pos in range(x + 1, max_x + 1):
                        if (x_pos, y, z) in coords:
                            probes += 1
                            break
                    for y_neg in range(min_y, y):
                        if (x, y_neg, z) in coords:
                            probes += 1
                            break
                    for y_pos in range(y + 1, max_y + 1):
                        if (x, y_pos, z) in coords:
                            probes += 1
                            break
                    for z_neg in range(min_z, z):
                        if (x, y, z_neg) in coords:
                            probes += 1
                            break
                    for z_pos in range(z + 1, max_z + 1):
                        if (x, y, z_pos) in coords:
                            probes += 1
                            break
                    if probes == 6:
                        internal_coords.append((x, y, z))

    visible_sides = 0
    for x, y, z in coords:
        for side in [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]:
            if side not in coords and side not in internal_coords:
                visible_sides += 1
    print(visible_sides)


if __name__ == "__main__":
    main()
