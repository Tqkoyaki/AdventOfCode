# Inputs the data
inp = open("daySeven/input.txt", "r")

# Node stores directories and their sizes
class Node:
    def __init__(self, name, val=0):
        self.name = name
        self.children = []
        self.val = val

# Tree holds file system
class Tree:
    def __init__(self):
        # Root is the root directory
        self.root = Node("/")
        # Stores the current directory being looked at
        self.cursor = [self.root]
    
    # Adds a new directory to the current directory 
    def new_dir(self, dir_name):
        self.cursor[-1].children.append(Node(dir_name))
    
    # Looks for the directory and moves cursor to it
    def forward(self, dir_name):
        for child in self.cursor[-1].children:
            if child.name == dir_name:
                self.cursor.append(child)
                return
    
    # Goes back to the parent directory in the cursor
    def backward(self):
        self.cursor.pop()
    
    # Resets the cursor to the root directory
    def reset(self):
        self.cursor = [self.root]
    
    # Updates all the sizes of the directories
    def update_sizes(self, val):
        for node in self.cursor:
            node.val += val

# Creates the data structure for file system
data = Tree()

# Loops through the input
for line in inp:
    # Strips newlines and splits the line
    line = line.strip().split(" ")
    
    # Numeric lines are file sizes
    if line[0].isnumeric():
        data.update_sizes(int(line[0]))
    # Dir are new directories
    elif line[0] == 'dir':
        data.new_dir(line[1])
    # Cd is the only command that affects the cursor or data
    elif line[1] == 'cd':
        # Goes back to the parent directory
        if line[2] == '..':
            data.backward()
        # Goes to the root directory
        elif line[2] == '/':
            data.reset()
        # Goes to the specified directory
        else:
            data.forward(line[2])


# Recursively sums the sizes of directories above the threshold
threshold = 100000
def recursive_sum(node):
    # Only adds the size if its below the threshold
    total = 0
    if node.val < threshold:
        total += node.val
    
    # Recursively adds the sizes of all the children
    for child in node.children:
        total += recursive_sum(child)
    
    return total

# Prints the answer
print(recursive_sum(data.root))