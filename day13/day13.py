import math

def get_data1():
    with open("day13.txt") as f:
        lines = f.read().split("\n")
    estimate = int(lines[0])
    bus_ids = [int(s) for s in lines[1].split(",") if s.isdigit()]
    return estimate, bus_ids


def part1():
    estimate, bus_ids = get_data1()
    bus_times = [0 for _ in bus_ids]
    for i in range(len(bus_ids)):
        while bus_times[i] < estimate:
            bus_times[i] += bus_ids[i]
    j = bus_times.index(min(bus_times))
    wait = bus_times[j] - estimate
    return bus_ids[j] * wait


def get_data2():
    with open("day13.txt") as f:
        lines = f.read().split("\n")
    digits = lines[1].split(",")
    bus_ids = [int(s) if s.isdigit() else None for s in digits]
    bus_departures = [t for t in range(len(bus_ids)) if bus_ids[t] is not None]
    bus_ids = [x for x in bus_ids if x is not None]
    return bus_ids, bus_departures


def part2():
    bus_ids, bus_departures = get_data2()
    ts = 0
    product = 1
    for i in range(len(bus_ids)):
        bus_id = bus_ids[i]
        bus_departure = bus_departures[i]
        # increment until we find a time that works for all buses so far
        while (ts + bus_departure) % bus_id != 0:
            ts += product
        # multiply by bus_id, so each increment will work for previous buses
        product *= bus_id
    return ts


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
    print(f"Part 2:\n{part2()}")
