import numpy as np

inp = open("dayEight/input.txt")

# Stores the grid data
grid = []

# Stores the highest score
score = 0

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
        left = grid[i, :j][::-1]
        right = grid[i, j+1:]
        top = grid[:i, j][::-1]
        bottom = grid[i+1:, j]
        
        # Edges are not counted
        if 0 in [len(left), len(right), len(top), len(bottom)]:
            continue
        
        # Gets the scores for each surrounding value
        try:
            left = [i >= val for i in left].index(True) + 1
        except:
            left = len(left)
        try:
            right = [i >= val for i in right].index(True) + 1
        except:
            right = len(right)
        try:
            top = [i >= val for i in top].index(True) + 1
        except:
            top = len(top)
        try:
            bottom = [i >= val for i in bottom].index(True) + 1
        except:
            bottom = len(bottom)
        
        # Determines if the current score is the highest
        if left * right * top * bottom > score:
            # Saves the highest score
            score = left * right * top * bottom

# Prints the highest score          
print(score)