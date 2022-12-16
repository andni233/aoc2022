import sys
import re


def main():
    rates = {}
    tunnels = {}

    m = r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)"
    for valve, rate, ts in [re.match(m, line).groups() for line in sys.stdin.readlines()]:
        tunnels[valve] = ts.split(", ")
        if rate := int(rate):
            rates[valve] = rate

    def _distances(start):
        distances = {start: 0}
        valves = [start]
        visited = [start]
        while valves and not all(v in distances.keys() for v in rates.keys()):
            valve = valves.pop(0)
            for step in tunnels[valve]:
                if step not in visited:
                    visited.append(step)
                    distances[step] = distances[valve] + 1
                    valves.append(step)
        return distances

    distances = {}
    for valve in ["AA"] + list(rates.keys()):
        distances[valve] = _distances(valve)

    def _paths(valve, path, remaining, time):
        for step in remaining:
            d = distances[valve][step] + 1
            if d < time:
                yield from _paths(step, path + [step], remaining - {step}, time - d)
        yield ["AA"] + path

    def _score(path, time):
        pressure_released = 0
        prev_valve = path[0]
        for valve in path[1:]:
            time -= distances[prev_valve][valve] + 1
            pressure_released += rates[valve] * time
            prev_valve = valve
        return pressure_released

    valves_with_rates = set(rates.keys())
    print(max([_score(path, 30) for path in _paths("AA", [], valves_with_rates, 30)]))


if __name__ == "__main__":
    main()
