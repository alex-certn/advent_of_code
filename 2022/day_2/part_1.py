from __future__ import annotations


file = open("day_2/input", "r")
input = file.read()
matches = input.split("\n")

class Shape:
    shape_map = {
        "A": "A",
        "B": "B",
        "C": "C",
        "X": "A",
        "Y": "B",
        "Z": "C",
    }
    
    points_map = {
        "A": 1,
        "B": 2,
        "C": 3,
    }

    def __init__(self, shape) -> None:
        self.shape = self.shape_map[shape]
        
    def __eq__(self, other: Shape) -> bool:
        return self.shape == other.shape
        
    def __gt__(self, other: Shape) -> bool:
        if self.shape == "C" and other.shape == "A":
            return False
        if self.shape == "A" and other.shape == "C":
            return True
        return self.shape > other.shape
    
    @property
    def points(self) -> int:
        return self.points_map[self.shape]   

def points(opponent_shape: str, your_shape: str) -> int:
    o_shape = Shape(shape=opponent_shape)
    y_shape = Shape(shape=your_shape)

    total = y_shape.points
    if y_shape == o_shape:
        total += 3
    if y_shape > o_shape:
        total += 6
    return total
    
total = 0
for match in matches:
    shapes = match.split(" ")
    o_shape = shapes[0]
    y_shape = shapes[1]
    total += points(o_shape, y_shape)
print(total)
