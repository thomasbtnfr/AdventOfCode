def read_data(filename):
    with open(filename, 'r') as f:
        return f.readline()

data = read_data("data.txt")    

# Part 1
# Find the first substring of length 4 with 4 unique characters
start = 0
end = 3
length = 4
num_unique_chars = 4

for i in range(len(data)-length):
    substring = data[start+i:end+i+1]
    if len(set(substring)) == num_unique_chars:
        start += i
        end += i
        break

print(end+1)

# Part 2
# Find the first substring of length 14 with 14 unique characters
start = 0
end = 13
length = 14
num_unique_chars = 14

for i in range(len(data)-length):
    substring = data[start+i:end+i+1]
    if len(set(substring)) == num_unique_chars:
        start += i
        end += i
        break

print(end+1)