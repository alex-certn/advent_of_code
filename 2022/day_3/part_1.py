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

for rucksack in rucksacks:
    length = len(rucksack)
    compartment_a = list(rucksack[:length//2])
    compartment_b = list(rucksack[length//2:])
    
    items_a = set(compartment_a)
    items_b = set(compartment_b)
    
    duplicate_items = items_a.intersection(items_b)

    for item in duplicate_items:
        total += character_value(item)

print(total)
