import re

state, instructions = [l.split('\n') for l in open("data.txt", "r").read().split('\n\n')]

# Initialize stacks with a len of 9
stacks = [[] for _ in state[-1].split()]


for line in state[:-1]:
    j=0
    for i in range(1, len(line), 4):
        if line[i] != ' ':
            stacks[j].append(line[i])
        j+=1
        
        
for instruction in instructions:
    groups = re.match(r'move (\d+) from (\d+) to (\d+)', instruction).groups()
    amount = int(groups[0])
    src = int(groups[1])
    dest = int(groups[2])
    
    for i in range(amount):
        stacks[dest-1].insert(0, stacks[src-1][amount-1-i])
        
    stacks[src-1] = stacks[src-1][amount:]

print("".join(stack[0] for stack in stacks))