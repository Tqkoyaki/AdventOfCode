inp = open('daySix/input.txt', 'r')

inp = list(inp.readline().strip())
buffer = inp[:14]

for i in range(len(inp)):
    # Adds letter to buffer
    buffer.append(inp[i])
    buffer = buffer[-14:]
    
    # First marker is reached
    if len(set(buffer)) == 14:
        print(i + 1)
        break
    
    