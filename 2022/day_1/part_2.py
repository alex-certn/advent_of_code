file = open("day_1/input", "r")
input = file.read()
elves = input.split("\n\n")

calories = [sum(map(lambda x: int(x), elf.split('\n'))) for elf in elves]

max_cal = max(calories)
total = max_cal

calories.remove(max_cal)
max_cal = max(calories)
total += max_cal

calories.remove(max_cal)
max_cal = max(calories)
total += max_cal

print(total)
