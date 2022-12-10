file = open("day_10/input", "r")
input = file.readlines()

cycle = 0
register_x = 1
save_points = [20,60,100,140,180,220]
signal_strength = []

for command in input:
    if len(save_points) == 0:
        break

    if command.startswith("noop"):
        cycle += 1

    if command.startswith("add"):
        cycle += 2

        value = int(command.split(' ')[1])

        if cycle >= save_points[0]:
            sp = save_points.pop(0)
            signal_strength.append(sp * register_x)

        register_x += value
        
print(sum(signal_strength))
