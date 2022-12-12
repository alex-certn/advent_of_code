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

for i in range(20):
    for monkey in monkeys:
        for old in monkey.items:
            monkey.action_counter += 1
            worry = eval(monkey.operation)
            worry = worry // 3
            if worry % monkey.test:
                monkeys[monkey.false_monkey].items.append(worry)
            else:
                monkeys[monkey.true_monkey].items.append(worry)
        monkey.items = []

actions = [m.action_counter for m in monkeys]
actions.sort()

print(actions[-1] * actions[-2])

