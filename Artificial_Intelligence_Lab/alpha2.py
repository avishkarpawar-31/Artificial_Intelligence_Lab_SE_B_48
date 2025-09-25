import math

# Node class definition for the game tree
class Node:
    def __init__(self, value=None, children=None):
        self.value = value  # Heuristic value for leaf nodes
        self.children = children or []

    def is_terminal(self):
        return len(self.children) == 0

    def evaluate(self):
        return self.value


def alpha_beta(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or node.is_terminal():
        return node.evaluate()

    if maximizingPlayer:
        value = -math.inf
        for child in node.children:
            value = max(value, alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                break  # Beta cut-off
        return value
    else:
        value = math.inf
        for child in node.children:
            value = min(value, alpha_beta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break  # Alpha cut-off
        return value


# Example Tree Construction:
#            root
#          /      \
#       n1          n2
#     / | \        /  \
#    3  5  6      9    1

leaf1 = Node(value=3)
leaf2 = Node(value=5)
leaf3 = Node(value=6)
leaf4 = Node(value=9)
leaf5 = Node(value=1)

n1 = Node(children=[leaf1, leaf2, leaf3])
n2 = Node(children=[leaf4, leaf5])
root = Node(children=[n1, n2])

optimal_value = alpha_beta(root, depth=3, alpha=-math.inf, beta=math.inf, maximizingPlayer=True)
print("Optimal value (with Alpha-Beta Pruning):", optimal_value)

