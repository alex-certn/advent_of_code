from functools import reduce
import operator


file = open("day_7/input", "r")
input = file.read()
lines = input.splitlines()


directories = {}
dir_path = []
for line in lines:
    if line == "$ cd ..":
        dir_path.pop(len(dir_path) - 1)
    elif line.startswith("$ cd"):
        name = line.split(" ")[-1]
        directory = reduce(operator.getitem, dir_path, directories)
        directory[name] = {"size": 0}
        dir_path.append(name)
    elif line.startswith("$ ls"):
        pass
    elif line.startswith("dir"):
        pass
    else:
        directory = reduce(operator.getitem, dir_path, directories)
        directory["size"] += int(line.split(" ")[0])

total = 0


def dig(new_directories: dict) -> int:
    global total
    keys_to_dig = set(new_directories.keys()) - {"size"}
    directory_size = new_directories.get("size", 0)

    for key in keys_to_dig:
        directory_size += dig(new_directories[key])

    if directory_size <= 100_000:
        total += directory_size

    return directory_size


dig(directories)

print(total)
