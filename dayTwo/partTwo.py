# A: Rock, B: Paper, C: Scissors Enemy
# Pick Points: 1 for Rock, 2 for Paper, 3 for Scissors
# Plus 0 for losing, 6 for winning, 3 for tie
# x means lose, y means draw, z means win


inp = open("dayTwo\input.txt", "r")

# Helps get choices using ASCII values
base = ord("A")
base_2 = ord("X")

# Loop up table for points
pickedTable = [0, 1, 2]

total = 0
for line in inp:
    # Seperate the two choices
    line = line.split(" ")
    
    # What was picked
    enemy = ord(line[0].strip()) - base
    strat = ord(line[1].strip()) - base_2
    
    # Adds strategy points
    total += (3 * strat)
    
    # Adds points based on what was picked
    total += pickedTable[(enemy + (strat - 1)) % 3] + 1
print(total)
    
    
    
    