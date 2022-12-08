with open('data.txt') as f:
    grid = f.read().splitlines()
    
nb_rows = len(grid)
nb_cols = len(grid[0])

scores = []

for i in range(1, nb_rows-1):
    for j in range(1, nb_cols-1):
        top = 0
        right = 0
        left = 0
        bottom = 0
        
        for k in range(i, 0, -1):
            top += 1
            if grid[k-1][j] >= grid[i][j]:
                break
            
        for k in range(j+1, nb_cols):
            right += 1
            if grid[i][k] >= grid[i][j]:
                break
            
        for k in range(j, 0, -1):
            left += 1
            if grid[i][k-1] >= grid[i][j]:
                break
            
        for k in range(i+1, nb_rows):
            bottom += 1
            if grid[k][j] >= grid[i][j]:
                break
        
        scores.append(top*right*left*bottom)
          
print(max(scores))