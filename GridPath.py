import random
def largest_grid_path(grid):
    x = len(grid)
    y = len(grid[0])
    j = random.randrange(y) # Random column starting point, either beginning or end of row
    sum = 0

    for i in range(x):
        if j == 0:
            for j in range(y):
                sum += grid[i][j]

        else: 
            for j in range(y - 1, -1, -1): # Iterate in reverse to continue path
                sum += grid[i][j]
 
    return sum
    


grid1 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

grid2 = [
  [5, 3],
  [2, 8]
]

print(largest_grid_path(grid1))
# 45 // (1 → 2 → 3 → 6 → 5 → 4 → 7 → 8 → 9) or (3 → 2 → 1 → 4 → 5 → 6 → 9 → 8 → 7)

print(largest_grid_path(grid2))
# 18 // (5 → 3 → 8 → 2) or (3 → 5 → 2 → 8)
