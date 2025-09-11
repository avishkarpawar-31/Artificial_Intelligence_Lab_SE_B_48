# Graph definition
graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'B': 2, 'C': 5, 'D': 12},
    'B': {'C': 2},
    'C': {'D': 3, 'G': 7},
    'D': {'G': 2},
    'G': {}
}

# Heuristic values
heuristics = {
    'S': 7, 'A': 6, 'B': 4,
    'C': 2, 'D': 1, 'G': 0
}

def a_star_search(graph, heuristics, start, goal):
    open_list = set([start])
    closed_list = set()

    # Stores actual cost from start to the node
    g = {start: 0}
    # Stores total estimated cost from start to goal through the node
    f = {start: heuristics[start]}
    # Parent dictionary to reconstruct path
    parent = {}

    while open_list:
        # Select node with lowest f(n)
        current = min(open_list, key=lambda node: f.get(node, float('inf')))
        
        if current == goal:
            # Reconstruct path
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path, g[goal]

        open_list.remove(current)
        closed_list.add(current)

        for neighbor, cost in graph[current].items():
            if neighbor in closed_list:
                continue

            tentative_g = g[current] + cost

            if neighbor not in open_list:
                open_list.add(neighbor)
            elif tentative_g >= g.get(neighbor, float('inf')):
                continue

            # This path is the best until now, record it
            parent[neighbor] = current
            g[neighbor] = tentative_g
            f[neighbor] = g[neighbor] + heuristics.get(neighbor, float('inf'))

    return None, float('inf')

start, goal = 'S', 'G'
path, cost = a_star_search(graph, heuristics, start, goal)

if path:
    print(f"Path found: {' -> '.join(path)}")
    print(f"Total cost: {cost}")
else:
    print("No path found.")

