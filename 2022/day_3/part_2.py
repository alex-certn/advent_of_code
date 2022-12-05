file = open("day_3/input", "r")
input = file.read()
rucksacks = input.split("\n")



def character_value(char: str) -> int:
    lowercase_offset = 97
    uppercase_offset = 65

    value = ord(char)

    if value >= lowercase_offset:
        return value - lowercase_offset + 1
    return value - uppercase_offset + 27


total = 0

while rucksacks:
    group = rucksacks[:3]

    group = [set(list(i)) for i in group]
    duplicate_items = group[0].intersection(group[1].intersection(group[2]))

    for item in duplicate_items:
        total += character_value(item)
        
    del rucksacks[:3]

print(total)
