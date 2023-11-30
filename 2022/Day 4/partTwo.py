import re

inp = open("dayFour\input.txt", "r")

total = 0

for line in inp:
    # Strips any newlines from the line
    line = line.strip()
    
    # Seperates and cleans the two pairs
    line = re.split("[, -]", line)
    line = [int(x) for x in line]
    
    # Lists all the numbers in the ranges
    line = list(range(line[0], line[1] + 1)) + list(range(line[2], line[3] + 1))
    
    # Checks if there are any duplicates
    if len(line) != len(set(line)):
        total += 1

print(total)