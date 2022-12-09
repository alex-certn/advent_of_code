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
head_location = Point()
tail_location = Point()

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
            
        if direction in ['L', 'R']:
            if head_location.x - tail_location.x > 1:
                tail_location.y = head_location.y
                tail_location.x += 1
            if head_location.x - tail_location.x < -1:
                tail_location.y = head_location.y
                tail_location.x -= 1
                
        if direction in ['U', 'D']:
            if head_location.y - tail_location.y > 1:
                tail_location.x = head_location.x
                tail_location.y += 1
            if head_location.y - tail_location.y < -1:
                tail_location.x = head_location.x
                tail_location.y -= 1

        visited.add((tail_location.x, tail_location.y))

print(len(visited))
