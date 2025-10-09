def alpha_beta(node, alpha, beta, is_max):
    # If leaf node (int), return value directly
    if isinstance(node, int):
        return node
    
    if is_max:
        value = -float('inf')
        for child in node:
            value = max(value, alpha_beta(child, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break  # Beta cutoff
        return value
    else:
        value = float('inf')
        for child in node:
            value = min(value, alpha_beta(child, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break  # Alpha cutoff
        return value

# Define the tree structure:
# d = [2,3]
d = [2, 3]

# e = [5,9]
e = [5, 9]

# f = [0,1]
f = [0, 1]

# g = [7,9]
g = [7, 9]

# b = [d, e]
b = [d, e]

# c = [f, g]
c = [f, g]

# a = [b, c]
a = [b, c]

# Run alpha-beta from root (MAX)
result = alpha_beta(a, -float('inf'), float('inf'), True)
print("Alpha-Beta value of root a:", result)

