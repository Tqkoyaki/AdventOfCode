inp = open("dayOne\input.txt", "r")

total = 0
# Holds all three maximum calories
maximum = [0, 0, 0]

for line in inp:
    # Verify that the line is not empty
    if line.strip() != "":
        total += int(line)
        continue
    
    # Appends the total because the line was empty
    maximum.append(total)
    # Removes the smallest value leaving the three largest
    maximum.remove(min(maximum))
    total = 0

# Sums the maximum before printing
print("The maximum calories the top three elf have is: " + str(sum(maximum)))