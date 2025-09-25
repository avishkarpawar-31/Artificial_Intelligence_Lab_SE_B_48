def minimax(node, is_max):
    # If node is a leaf (int), return its value directly
    if isinstance(node, int):
        return node
    
    if is_max:
        best_value = -float('inf')
        for child in node:
            val = minimax(child, False)  # next is MIN
            best_value = max(best_value, val)
        return best_value
    else:
        best_value = float('inf')
        for child in node:
            val = minimax(child, True)  # next is MAX
            best_value = min(best_value, val)
        return best_value

# Define the tree
# d has children m=3, e=12, f=8
d = [3, 12, 8]

# c has children g=2, h=4, i=6
c = [2, 4, 6]

# b has children j=14, k=5, l=2
b = [14, 5, 2]

# a has children d, c, b
a = [d, c, b]

# Run minimax from root (MAX)
result = minimax(a, True)
print("Minimax value of root a:", result)

