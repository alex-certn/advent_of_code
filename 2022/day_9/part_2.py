from dataclasses import dataclass


file = open("day_9/input", "r")
input = file.readlines()

@dataclass
class Point:
    x: int = 0
    y: int = 0
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

visited = set()
rope = [Point(), Point(), Point(), Point(), Point(), Point(), Point(), Point(), Point(), Point()]
tail_location = rope[-1]
head_location = rope[0]

def move_rope(head, tail) -> bool:
    difference_x = abs(head.x - tail.x)
    difference_y = abs(head.y - tail.y)
    
    if (difference_x > 1 or difference_y > 1) and (difference_x != 0 and difference_y != 0):
        tail.x += (head.x - tail.x) / difference_x
        tail.y += (head.y - tail.y) / difference_y
        return True
    if difference_x > 1:
        tail.x += (head.x - tail.x) / difference_x
        return True
    if difference_y > 1:
        tail.y += (head.y - tail.y) / difference_y
        return True

    return False

for move in input:
    direction = move.split(" ")[0]
    distance = int(move.split(" ")[1])

    for i in range(distance):
        if direction == 'R':
            head_location.x += 1
        if direction == 'L':
            head_location.x -= 1
        if direction == 'U':
            head_location.y += 1
        if direction == 'D':
            head_location.y -= 1

        for index in range(len(rope) - 1):
            moved = move_rope(rope[index], rope[index+1])
            if not moved:
                break

        visited.add((tail_location.x, tail_location.y))

print(len(visited))
