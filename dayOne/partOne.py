inp = open("dayOne\input.txt", "r")

total = 0
maximum = 0

for line in inp:
    # Verify that the line is not empty
    if line.strip() != "":
        # Adds to total and skips to next loop
        total += int(line)
        continue

    # The line was empty so we check for maximum
    if total > maximum:
        maximum = total
    total = 0

print("The maximum calories one elf has: " + str(maximum))