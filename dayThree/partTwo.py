inp = open("dayThree\input.txt", "r")

total = 0
counter = 0

elves = []
unique = []

for line in inp:
    # Updates data with clean line
    line = line.strip()
    elves.append(set(line))
    counter += 1
    
    # Every 3rd iteration
    if counter % 3 == 0:
        for dups in elves[0].intersection(elves[1], elves[2]):
            # Adds based on priority
            if dups.islower():
                total += ord(dups) - 96
            else:
                total += ord(dups) - 38
        elves = []

print(total)
    
    
    
    