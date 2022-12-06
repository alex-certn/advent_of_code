file = open("day_6/input", "r")
input = file.read()

window = []
for index, char in enumerate(list(input)):
    window.append(char)
    if len(window) > 14:
        window.pop(0)
    if len(set(window)) == 14:
        print(index + 1)
        break
