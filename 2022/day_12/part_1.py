from dataclasses import dataclass
from typing import List


file = open("day_12/input", "r")
input = file.readlines()
graph = [[ord(j) for j in list(i.strip())] for i in input]

@dataclass
class Point:
    x: int
    y: int
    
    def __hash__(self):
        return x ** (y * 100)
    
    def __str__(self) -> str:
        return f"({self.x},{self.y})"

def neighbours(point: Point) -> List[Point]:
    valid = []
    value = graph[point.y][point.x]

    up = Point(point.x, point.y - 1)
    down = Point(point.x, point.y + 1)
    left = Point(point.x - 1, point.y)
    right = Point(point.x + 1, point.y)

    neighbours = [up, down, left, right]

    for neighbour in neighbours:
        if neighbour.y < 0 or neighbour.x < 0 or neighbour.y > len(graph) - 1 or neighbour.x > len(graph[0]) - 1:
            continue
        if value == ord('E') and graph[neighbour.y][neighbour.x] == ord('z'):
            valid.append(neighbour)
            continue
        if value == ord('E') and graph[neighbour.y][neighbour.x] != ord('z'):
            continue
        if value == ord('a') and graph[neighbour.y][neighbour.x] == ord('S'):
            return [neighbour]
        if value > 1 + graph[neighbour.y][neighbour.x]:
            continue
        
        valid.append(neighbour)
    
    return valid

visited = []
queue = []

def search(visited, point):
    path_length = 0

    visited.append(point)
    queue.append(point)

    while queue:
        size = len(queue)
        for _ in range(size):
            current = queue.pop(0)
            if graph[current.y][current.x] == ord('S'):
                return path_length
            for neighbour in neighbours(current):
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        path_length += 1


starting_point = None
for y, row in enumerate(graph):
    for x, col in enumerate(row):
        if graph[y][x] == ord('E'):
            starting_point = Point(x, y)
            break
    if starting_point:
        break

print(search(visited, starting_point))
