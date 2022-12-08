from collections import Counter
from itertools import islice

def readfile(filename):
    with open(filename, 'r') as f:
        files = f.read().splitlines()
    return files

def letterToNumbers(char):
    if not char.isupper():
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 27

def readGroups(filename):
    file = []
    with open(filename, 'r') as f:
        while True:
            next_n_lines = list(islice(f, 3))
            next_n_lines = [line.replace("\n", "") for line in next_n_lines]
            if not next_n_lines:
                break
            else:
                file.append(next_n_lines)
    return file


# Part 1
bags = readfile('data.txt')
total_score = 0

for bag in bags:
    first_half = bag[:len(bag)//2]
    second_half = bag[len(bag)//2:]
    common_caracter = ''.join(set(first_half).intersection(set(second_half)))
    total_score += letterToNumbers(common_caracter)

print(total_score)

# Part 2
groups = readGroups('data.txt')
total_score = 0
for group in groups:
    common_caracter = set(group[0]).intersection(*group)
    total_score += letterToNumbers(common_caracter.pop())

print(total_score)