# A: Rock, B: Paper, C: Scissors
# X: Rock, Y: Paper, Z: Scissors
# Pick Points: 1 for Rock, 2 for Paper, 3 for Scissors
# Plus 0 for losing, 6 for winning, 3 for tie


inp = open("dayTwo\input.txt", "r")

# Helps get choices using ASCII values
base = ord("A")
base_2 = ord("X")

# Loop up table for points
point_table = [[3, 0, 6],
               [6, 3, 0],
               [0, 6, 3]]

total = 0
for line in inp:
    # Seperate the two choices
    line = line.split(" ")
    
    # What was picked
    enemy = ord(line[0].strip()) - base
    picked = ord(line[1].strip()) - base_2
    
    total += point_table[picked][enemy] + picked + 1

print(total)
    
    
    
    