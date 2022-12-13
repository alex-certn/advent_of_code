file = open("day_13/input", "r")
input = file.readlines()

packets = []
for i in input:
    cleaned = i.strip()
    if cleaned:
        packets.append(eval(i))
    else:
        packets.append(None)
     
def compare(left, right) -> int:
    max_index = max([len(left), len(right)])
    for i in range(max_index):
        try:
            l = left[i]
        except IndexError:
            return 1  # If the left list runs out of items first, the inputs are in the right order.
        try:
            r = right[i]
        except IndexError:
            return 2  # If the right list runs out of items first, the inputs are not in the right order.

        if type(l) != type(r):  # If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison.
            if type(l) != list:
                l = [l]
            elif type(r) != list:
                r = [r]

        if type(l) == list:
            result = compare(l, r)  # If both values are lists, compare the first value of each list, then the second value, and so on.
            if result == -1:
                continue
            else:
                return result

        if l < r:
            return 1  # If the left integer is lower than the right integer, the inputs are in the right order.
        if l > r:
            return 2  # If the left integer is higher than the right integer, the inputs are not in the right order.

    return -1

ordered_packets = []
pair_count = 1

while packets:
    left = packets.pop(0)
    right = packets.pop(0)

    is_ordered = compare(left, right)
    
    if is_ordered == 1:
        ordered_packets.append(pair_count)
    
    if packets:
        packets.pop(0)  # None

    pair_count += 1

print(sum(ordered_packets))
