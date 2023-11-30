import numpy as np

inp = open("dayEight/input.txt")

# Holds the grid data
grid = []

# Tracker for the number of visible trees
visible = 0

# Moves data into a 2D matrix
for line in inp:
    # Removes newlines
    line = line.strip()
    
    # Splits the characters of the line
    line = [*line]
    
    # Converts data to integers
    line = [int(i) for i in line]
    
    # Adds to grid array
    grid.append(line)

# Converts to numpy array
grid = np.array(grid)

# # Loops through the grid
for i in range(len(grid)):
    for j in range(len(grid[i])):
        # Gets the value currently being looked at
        val = grid[i, j]
        
        # Checks all the values around it
        left = grid[i, :j]
        right = grid[i, j+1:]
        top = grid[:i, j]
        bottom = grid[i+1:, j]
        
        try:
            # Gets the checks for the surrounding values
            checks = [left.max(), right.max(), top.max(), bottom.max()]
            
            # Checks if the value is the largest of the surrounding values
            if val > min(checks):
                visible += 1
        except:
            visible += 1
print(visible)