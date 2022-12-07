inp = open('dayFive/input.txt', 'r')

# Data structure for crates
crates = [[] for i in range(9)]

# Loops through crate schema
line = inp.readline()
while True:
    # Ignores after crate schema is complete
    if line.replace(" ", "").strip().isnumeric():
        break
    
    # Splits the line into a list of characters
    line = [*line[1::4]]
    
    # Appends each section appropriately
    for i in range(9):
        if line[i] != ' ':
            crates[i].append(line[i])
    
    # Updates line
    line = inp.readline()

# Reverses each list for stacks
for i in range(len(crates)):
    crates[i] = crates[i][::-1]
    
# Skips the empty line
line = inp.readline()

# Loops through the moves
for line in inp:
    # Gets only the numbers
    line = line.split()[1::2]
    
    # Moves each crate to new stack and removes from old stack
    for i in range(int(line[0])):
        crates[int(line[2]) - 1].append(crates[int(line[1]) - 1].pop())

# Appends the top of each stack to a string to get the result
res = ''
for i in range(len(crates)):
    res += crates[i].pop()

print(res)
    


    