from functools import reduce
import operator


file = open("day_7/input", "r")
input = file.read()
lines = input.splitlines()


directories = {}
dir_path = []
used_space = 0
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
        used_space += int(line.split(" ")[0])

available_space = 70_000_000 - used_space
min_to_delete = 30_000_000 - available_space
smallest_folder_to_delete = 70_000_000


def dig(new_directories: dict) -> int:
    global smallest_folder_to_delete
    keys_to_dig = set(new_directories.keys()) - {"size"}
    directory_size = new_directories.get("size", 0)

    for key in keys_to_dig:
        directory_size += dig(new_directories[key])

    if directory_size >= min_to_delete and directory_size < smallest_folder_to_delete:
        smallest_folder_to_delete = directory_size

    return directory_size


dig(directories)

print(smallest_folder_to_delete)
