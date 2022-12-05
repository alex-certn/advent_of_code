file = open("day_1/input", "r")
input = file.read()
elves = input.split("\n\n")

print(
    max(
        [sum(map(lambda x: int(x), elf.split('\n'))) for elf in elves]
    )
)
