def readdata(file):
    with open(file, 'r') as f:
        file = [section.split() for section in f.read().split('\n\n')]
    return file

file = readdata('data.txt')

# 1
print(max(sum(map(int, lutin)) for lutin in file))

# 2
sums = [sum(map(int, lutin)) for lutin in file]
print(sum(sorted(sums, reverse=True)[:3]))