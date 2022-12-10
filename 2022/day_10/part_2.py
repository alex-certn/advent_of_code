from math import floor


file = open("day_10/input", "r")
input = file.readlines()

cycle = 0
register_x = 1

screen = [
    ['.'] * 40,
    ['.'] * 40,
    ['.'] * 40,
    ['.'] * 40,
    ['.'] * 40,
    ['.'] * 40
]

def draw(screen_index: int, sprite_center: int):
    global screen
    row = floor(screen_index / 40)
    index = screen_index % 40
    
    if index in [sprite_center - 1, sprite_center, sprite_center + 1]:
        screen[row][index] = '#'

for command in input:
    if command.startswith("noop"):
        draw(cycle, register_x)
        cycle += 1

    if command.startswith("add"):
        draw(cycle, register_x)
        draw(cycle + 1, register_x)

        cycle += 2

        value = int(command.split(' ')[1])

        register_x += value
        
        
[print("".join(i)) for i in screen]
