import re

inp = open("dayFour\input.txt", "r")

total = 0

for line in inp:
    # Strips any newlines from the line
    line = line.strip()
    
    # Seperates and cleans the two pairs
    line = re.split("[, -]", line)
    line = [int(x) for x in line]
    
    # Seperates the pairs for checking
    pairs = [line[0:2], line[2:4]]
    
    # Checks if there is a pair that can take the other pair as a subset
    if [min(line), max(line)] in pairs:
        total += 1

print(total)