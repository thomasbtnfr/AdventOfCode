with open('data.txt') as f:
    grid = f.read().splitlines()
    
nb_rows = len(grid)
nb_cols = len(grid[0])

nb_borders = nb_rows*2 + (nb_cols-2)*2

nb_visible = 0
for i in range(1, nb_rows-1):
    for j in range(1, nb_cols-1):
        top = True
        right = True
        left = True
        bottom = True
        
        for k in range(0, i):
            if grid[k][j] >= grid[i][j]:
                top = False
                break
            
        for k in range(j+1, nb_cols):
            if grid[i][k] >= grid[i][j]:
                right = False
                break
            
        for k in range(0, j):
            if grid[i][k] >= grid[i][j]:
                left = False
                break
            
        for k in range(i+1, nb_rows):
            if grid[k][j] >= grid[i][j]:
                bottom = False
                break
            
        if top or right or left or bottom:
            nb_visible += 1
            
print(nb_visible+nb_borders)