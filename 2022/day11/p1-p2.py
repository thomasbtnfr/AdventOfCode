from collections import defaultdict
from functools import reduce

view_counter = defaultdict(int)
monkeys = [
    [54, 53],
    [95, 88, 75, 81, 91, 67, 65, 84],
    [76, 81, 50, 93, 96, 81, 83],
    [83, 85, 85, 63],
    [85, 52, 64],
    [57],
    [60, 95, 76, 66, 91],
    [65, 84, 76, 72, 79, 65]
]
if_true = [2, 3, 5, 7, 0, 1, 2, 6]
if_false = [6, 4, 1, 4, 7, 3, 5, 0]
operation = [
    lambda old: old*3,
    lambda old: old*11,
    lambda old: old+6,
    lambda old: old+4,
    lambda old: old+8,
    lambda old: old+2,
    lambda old: old*old,
    lambda old: old+5
]
divisible_by = [2, 7, 3, 11, 17, 5, 13, 19]

# Part 1
for _ in range(20):
    for i, monkey in enumerate(monkeys):
        while monkey:
            item = monkey.pop(0)
            view_counter[i] += 1
            worry_level_operation = operation[i](item)
            worry_level_d3 = worry_level_operation // 3
            worry_level_divisible_by = worry_level_d3 % divisible_by[i]
            
            print(item, worry_level_operation, worry_level_d3, worry_level_divisible_by)

            if worry_level_divisible_by == 0:
                monkeys[if_true[i]].append(worry_level_d3)
            else:
                monkeys[if_false[i]].append(worry_level_d3)

print(reduce(lambda x, y: x*y, sorted(view_counter.values())[-2:]))