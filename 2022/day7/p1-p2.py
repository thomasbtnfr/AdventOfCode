import re
from collections import defaultdict

def read_data(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

lines = read_data('data.txt')

directories_size = defaultdict(int)
structure = []

for l in lines:
    if l.startswith("$ cd"):
        cd_direction = re.search(r"cd (.*)", l).group(1)
        if cd_direction == "/":
            structure = []
        elif cd_direction == "..":
            structure.pop()
        else:
            structure.append(cd_direction)
    
    elif not l.startswith("$ ls"):
        a, _ = l.split()
        if a != "dir":
            for j in range(len(structure)+1):
                path = "/" + "/".join(structure[:j])
                directories_size[path] += int(a)

# Part 1 
print(sum(filter(lambda v: v <= 100000, directories_size.values())))

# Part 2
total_disk_space = 70000000
need = 30000000
used = directories_size['/']
unused = total_disk_space - used
space_needed = need - unused

print(min(filter(lambda s: s >= space_needed, directories_size.values())))


