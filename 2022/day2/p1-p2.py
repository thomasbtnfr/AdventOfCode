def readdata(file):
    with open(file, 'r') as f:
        file = [section.split() for section in f.read().split('\n')]
    return file

games = readdata('data.txt')

XYZ = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

possibilites = {
    'A X': 3,
    'A Y': 6,
    'A Z': 0,
    'B X': 0,
    'B Y': 3,
    'B Z': 6,
    'C X': 6,
    'C Y': 0,
    'C Z': 3
}

possibilites_part2 = {
    'A 3': 'X',
    'A 6': 'Y',
    'A 0': 'Z',
    'B 0': 'X',
    'B 3': 'Y',
    'B 6': 'Z',
    'C 6': 'X',
    'C 0': 'Y',
    'C 3': 'Z'
}

XYZ_goal = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

# Part 1
total_score = 0
for game in games:
    total_score += XYZ[game[1]] + possibilites[" ".join(game)]
print(total_score)

# Part 2
total_score = 0
for game in games:
    enemy_choice = game[0]
    score = XYZ_goal[game[1]]
    move_todo = possibilites_part2[" ".join([enemy_choice, str(score)])]
    total_score += score + XYZ[move_todo]

print(total_score)
    