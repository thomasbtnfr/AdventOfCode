with open('data.txt') as f:
    instructions = f.read().splitlines()

# Part 1
cycles_20_values = []
cycle_cpt = 0
value_cpt = 1
cycle_goal = 20

for instruction in instructions:
    operation = instruction.split()[0]
    if operation == "addx":
        number = int(instruction.split()[1])
        cycle_cpt += 2
        value_cpt += number
        if cycle_cpt == cycle_goal or cycle_cpt+1 == cycle_goal or cycle_cpt+2 == cycle_goal:
            cycles_20_values.append(cycle_goal*value_cpt)
            cycle_goal += 40
    else:
        cycle_cpt += 1
        if cycle_cpt == cycle_goal or cycle_cpt+1 == cycle_goal:
            cycles_20_values.append(cycle_goal*value_cpt)
            cycle_goal += 40

print(sum(cycles_20_values))