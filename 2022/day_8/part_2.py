from typing import List


file = open("day_8/input", "r")
input = file.read()
trees = [[int(i) for i in list(i)] for i in input.splitlines()]

def transpose(l: List[List]) -> List[List]:
    return [list(i) for i in zip(*l)]

def get_scored_grid(input: List[List[int]]) -> List[List[int]]:
    max_x = len(input)
    max_y = len(input[0])

    scoring_grid = [[0] * max_x for i in range(max_y)]

    for y in range(max_y):
        for x in range(max_x):
            house = input[y][x]

            visible_left = []
            for tree in input[y][:x][::-1]:
                visible_left.append(tree)
                if tree >= house:
                    break

            visible_right = []
            for tree in input[y][x+1:]:
                visible_right.append(tree)
                if tree >= house:
                    break

            scoring_grid[y][x] = len(visible_left) * len(visible_right)
                    

    return scoring_grid


scoring_grid_x = get_scored_grid(trees)
scoring_grid_y = transpose(get_scored_grid(transpose(trees)))


highest = -1
for x in range(len(scoring_grid_x[0])):
    for y in range(len(scoring_grid_x)):
        score = scoring_grid_x[x][y] * scoring_grid_y[x][y]
        if score > highest:
            highest = score

print(highest)
