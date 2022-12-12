from dataclasses import dataclass, field
from typing import List

file = open("day_11/input", "r")
input = file.readlines()

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

@dataclass
class Monkey:
    items: List[int] = field(default_factory=list)
    operation: str = ""
    test: int = -1
    true_monkey: int = -1
    false_monkey: int = -1
    action_counter = 0

input_monkeys = chunks(input, 7)
monkeys = []
for m in input_monkeys:
    starting_items = [int(i) for i in m[1].strip().split(': ')[-1].split(', ')]
    monkeys.append(
        Monkey(
            items=starting_items,
            operation=m[2].split('=')[-1].strip(),
            test=int(m[3].split('by ')[-1].strip()),
            true_monkey=int(m[4].split('monkey ')[-1].strip()),
            false_monkey=int(m[5].split('monkey ')[-1].strip())
        )
    )

def operation(i: int, old: int) -> int:
    if i == 0:
        return old * 5
    if i == 1:
        return old * 11
    if i == 2:
        return old + 2
    if i == 3:
        return old + 5
    if i == 4:
        return old * old
    if i == 5:
        return old + 4
    if i == 6:
        return old + 6
    if i == 7:
        return old + 7
    return -1

maxes = [i.test for i in monkeys]
max = 1
for i in maxes:
    max *= i
print(max)
for i in range(10_000):
    for index, monkey in enumerate(monkeys):
        for old in monkey.items:
            monkey.action_counter += 1
            worry = eval(monkey.operation)
            if worry > 2 * max:
                worry = max + (worry % max)
            if worry % monkey.test != 0:
                monkeys[monkey.false_monkey].items.append(worry)
            else:
                monkeys[monkey.true_monkey].items.append(worry)
        monkey.items = []
    if i in [0, 19, 999, 1999]:
        print([i.action_counter for i in monkeys])

actions = [m.action_counter for m in monkeys]
print(actions)
actions.sort()
print(actions)
print(actions[-1] * actions[-2])

