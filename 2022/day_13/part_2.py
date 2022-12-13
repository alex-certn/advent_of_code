from functools import cmp_to_key


file = open("day_13/input", "r")
input = file.readlines()

packets = []
for i in input:
    cleaned = i.strip()
    if cleaned:
        packets.append(eval(i))

packets.append([[2]])
packets.append([[6]])

     
def compare(left, right) -> int:
    max_index = max([len(left), len(right)])
    for i in range(max_index):
        try:
            l = left[i]
        except IndexError:
            return -1  # If the left list runs out of items first, the inputs are in the right order.
        try:
            r = right[i]
        except IndexError:
            return 1  # If the right list runs out of items first, the inputs are not in the right order.

        if type(l) != type(r):  # If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison.
            if type(l) != list:
                l = [l]
            elif type(r) != list:
                r = [r]

        if type(l) == list:
            result = compare(l, r)  # If both values are lists, compare the first value of each list, then the second value, and so on.
            if result == 0:
                continue
            else:
                return result

        if l < r:
            return -1  # If the left integer is lower than the right integer, the inputs are in the right order.
        if l > r:
            return 1  # If the left integer is higher than the right integer, the inputs are not in the right order.

    return 0

sorted_packets = sorted(packets, key=cmp_to_key(compare))

packet_a = None
packet_b = None

for index, packet in enumerate(sorted_packets):
    if packet == [[2]]:
        packet_a = index + 1
    if packet == [[6]]:
        packet_b = index + 1
    if packet_a and packet_b:
        print(packet_a * packet_b)
        break
