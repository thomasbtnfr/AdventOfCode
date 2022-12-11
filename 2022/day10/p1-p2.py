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


# Part 2
cycles_20_values = []
cycle_cpt = 0
value_cpt = 1
cycle_goal = 40
res = []
sprite = [1, 2, 3]

for instruction in instructions:
    operation = instruction.split()[0]
    if operation == "addx":
        number = int(instruction.split()[1])
        cycle_cpt += 2
        value_cpt += number

        res.append('#') if cycle_cpt-1 in sprite else res.append('.')
        if cycle_cpt-1 == cycle_goal:
            cycle_cpt=1
        res.append('#') if cycle_cpt in sprite else res.append('.')
        if cycle_cpt == cycle_goal:
            cycle_cpt=0

        sprite = [value_cpt, value_cpt+1, value_cpt+2]

    else:
        cycle_cpt += 1
        res.append('#') if cycle_cpt in sprite else res.append('.')
        if cycle_cpt == cycle_goal:
            cycle_cpt=0

        sprite = [value_cpt, value_cpt+1, value_cpt+2]
    
for i in range(0, 240, 40):
    print("".join(res[i:i+40]))

