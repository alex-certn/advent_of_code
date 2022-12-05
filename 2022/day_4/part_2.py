file = open("day_4/input", "r")
input = file.read()
pairs = input.split("\n")

total = 0
for pair in pairs:
    ranges = pair.split(",")
    bound_a = ranges[0].split("-")
    bound_b = ranges[1].split("-")
    set_a = set(range(int(bound_a[0]), int(bound_a[1]) + 1))
    set_b = set(range(int(bound_b[0]), int(bound_b[1]) + 1))

    if set_a.intersection(set_b) or set_b.intersection(set_a):
        total += 1

print(total)
