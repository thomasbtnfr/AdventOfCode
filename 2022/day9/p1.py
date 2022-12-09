def move(head_position, direction):
    match direction:
        case "R": head_position[0] += 1
        case "L": head_position[0] -= 1
        case "U": head_position[1] += 1
        case "D": head_position[1] -= 1
    return head_position

def follow(tail, head):
    tail_x, tail_y = tail[0], tail[1]
    head_x, head_y = head[0], head[1]
    
    if abs(head_x - tail_x) > 1 or abs(head_y - tail_y) > 1:
        if tail_x == head_x:
            tail_y += 1 if head_y > tail_y else -1
        elif tail_y == head_y:
            tail_x += 1 if head_x > tail_x else -1
        else:
            tail_x += 1 if head_x > tail_x else -1
            tail_y += 1 if head_y > tail_y else -1
    return (tuple([tail_x, tail_y]))




head = [0, 0]
tail = tuple([0, 0])
tail_visited = set()

with open('data.txt', 'r') as f:
    movements = f.read().splitlines()

    for m in movements:
        direction, nstep = m.split()
        print(direction, nstep)

        for _ in range(int(nstep)):
            head = move(head, direction)
            tail = follow(tail, head)

            tail_visited.add(tail)

print(len(tail_visited))