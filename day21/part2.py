import sys


def main():
    lines = []
    for line in sys.stdin.readlines():
        if "humn: " not in line:
            lines.append(line.replace(":", "").strip())

    monkeys = {}
    for line in lines:
        ds = tuple(line.split(" "))
        if len(ds) == 2:
            monkeys[ds[0]] = int(ds[1])
        else:
            monkeys[ds[0]] = (ds[1], ds[2], ds[3])

    def _simulate(monkey):
        if isinstance(monkeys[monkey], int) or isinstance(monkeys[monkey], float):
            return monkeys[monkey]
        lhs, op, rhs = monkeys[monkey]
        match op:
            case "+":
                return _simulate(lhs) + _simulate(rhs)
            case "-":
                return _simulate(lhs) - _simulate(rhs)
            case "/":
                return _simulate(lhs) // _simulate(rhs)
            case "*":
                return _simulate(lhs) * _simulate(rhs)

    root_lhs, root_rhs = monkeys["root"][0], monkeys["root"][-1]
    try:
        target = _simulate(root_lhs)
        path = root_rhs
    except KeyError:
        target = _simulate(root_rhs)
        path = root_lhs

    def _simulate_human(monkey, target):
        if monkey == "humn":
            return target
        lhs, op, rhs = monkeys[monkey]
        match op:
            case "+":
                try:
                    return _simulate_human(lhs, target - _simulate(rhs))
                except KeyError:
                    return _simulate_human(rhs, target - _simulate(lhs))
            case "-":
                try:
                    return _simulate_human(lhs, target + _simulate(rhs))
                except KeyError:
                    return _simulate_human(rhs, target + _simulate(lhs))
            case "/":
                try:
                    return _simulate_human(lhs, target * _simulate(rhs))
                except KeyError:
                    return _simulate_human(rhs, target * _simulate(lhs))
            case "*":
                try:
                    return _simulate_human(lhs, target // _simulate(rhs))
                except KeyError:
                    return _simulate_human(rhs, target // _simulate(lhs))

    print(_simulate_human(path, -target))


if __name__ == "__main__":
    main()
