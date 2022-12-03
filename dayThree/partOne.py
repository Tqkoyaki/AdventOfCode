inp = open("dayThree\input.txt", "r")

total = 0

for line in inp:
    # Strips any newlines from the line
    line = line.strip()
    
    # Splits into two compartments
    compart_one = line[:len(line) // 2]
    compart_two = line[len(line) // 2:]
    
    # Gets all unique types in each compartment
    compart_one = set(compart_one)
    compart_two = set(compart_two)

    # Gets duplicates between the two compartments
    for dups in compart_one.intersection(compart_two):
        # Adds based on priority
        if dups.islower():
            total += ord(dups) - 96
        else:
            total += ord(dups) - 38

print(total)
    
    
    
    