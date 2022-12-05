from __future__ import annotations


file = open("day_2/input", "r")
input = file.read()
matches = input.split("\n")

def points(o_shape, result) -> int:
    shape_points = [1, 2, 3, 1, 2, 3]
    starting_index = {
        "A": 0,
        "B": 1,
        "C": 2,
    }
    shift_amount = {
        "X": -1,
        "Y": 0,
        "Z": 1,
    }
    result_points = {
        "X": 0,
        "Y": 3,
        "Z": 6,
    }

    return result_points[result] + shape_points[starting_index[o_shape] + shift_amount[result]]
    
total = 0
for match in matches:
    shapes = match.split(" ")
    o_shape = shapes[0]
    result = shapes[1]
    total += points(o_shape, result)
print(total)
