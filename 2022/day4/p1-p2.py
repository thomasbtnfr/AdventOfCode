def readfile(filename):
    with open(filename, 'r') as f:
        files = f.read().splitlines()
    files = [file.split(',') for file in files]
    return files

def fullOverlap(elf0, elf1):
    if elf0[0] >= elf1[0] and elf0[1] <= elf1[1]:
        return 1
    elif elf1[0] >= elf0[0] and elf1[1] <= elf0[1]:
        return 1
    else:
        return 0

def partialOverlap(elf0, elf1):
    if fullOverlap(elf0, elf1) != 0:
        return 1
    if elf0[1] == elf1[0] or elf0[0] == elf1[1]:
        return 1
    if elf0[0] < elf1[0] and elf0[1] < elf1[1] and elf1[0] < elf0[1]:
        return 1
    elif elf0[0] > elf1[0] and elf0[1] > elf1[1] and elf0[0] < elf1[1]:
        return 1
    else:
        return 0 

files = readfile('data.txt')

# Part 1
total_score = 0
for pair in files:
    elf0 = list(map(int, pair[0].split('-')))
    elf1 = list(map(int, pair[1].split('-')))
    total_score += fullOverlap(elf0, elf1)

print(total_score)

# Part 2
total_score = 0
for pair in files:
    elf0 = list(map(int, pair[0].split('-')))
    elf1 = list(map(int, pair[1].split('-')))
    total_score += partialOverlap(elf0, elf1)

print(total_score)
