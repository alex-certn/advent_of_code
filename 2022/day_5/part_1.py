import re
from collections import deque

file = open("day_5/input", "r")
input = file.read()
lines = input.split("\n")

moves = lines[10:]
board = lines[:8]

stacks = []
for line in board:
    line_array = list(line)
    stacks.append(
        [
            line_array[1],
            line_array[5],
            line_array[9],
            line_array[13],
            line_array[17],
            line_array[21],
            line_array[25],
            line_array[29],
            line_array[33],
        ]
    )

stacks = list(zip(*stacks))
filtered_stacks = []
for stack in stacks:
    filtered_stacks.append(list(filter((' ').__ne__, stack)))

parsed_moves = []
for move in moves:
    parsed_moves.append([int(i) for i in re.findall(r'\d{1,2}', move)])

for move in parsed_moves:
    target = move[2] - 1
    source = move[1] - 1
    quantity = move[0]

    filtered_stacks[target] = [*filtered_stacks[source][:quantity][::-1], *filtered_stacks[target]]
    filtered_stacks[source] = filtered_stacks[source][quantity:]

print(''.join([i[0] for i in filtered_stacks if i]))
