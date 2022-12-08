from typing import List


file = open("day_8/input", "r")
input = file.read()
trees = [[int(i) for i in list(i)] for i in input.splitlines()]

def transpose(l: List[List]) -> List[List]:
    return [list(i) for i in zip(*l)]

def get_scored_grid(input: List[List[int]]) -> List[List[bool]]:
    max_x = len(input)
    max_y = len(input[0])

    scoring_grid = [[False] * max_x for i in range(max_y)]

    for y in range(max_y):
        reverse_y = -(y+1)

        if y == 0:
            scoring_grid[0] = [True] * max_x
            scoring_grid[-1] = [True] * max_x
            continue

        for x in range(max_x):
            reverse_x = -(x+1)

            if x == 0:
                scoring_grid[y][x] = True
                scoring_grid[y][reverse_x] = True
                scoring_grid[reverse_y][x] = True
                scoring_grid[reverse_y][reverse_x] = True
                continue

            left = input[y][:x]
            max_left = -1
            if left:
                max_left = max(left)
            right = input[y][x+1:]
            max_right = -1
            if right:
                max_right = max(right)
            scoring_grid[y][x] |= max_left < input[y][x] or max_right < input[y][x]

    return scoring_grid


scoring_grid_x = get_scored_grid(trees)
scoring_grid_y = transpose(get_scored_grid(transpose(trees)))

total = 0
for x in range(len(scoring_grid_x[0])):
    for y in range(len(scoring_grid_x)):
        if scoring_grid_x[x][y] or scoring_grid_y[x][y]:
            total += 1

print(total)
