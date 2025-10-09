# Graph definition
graph = {
    'Home': {'School': 50, 'Garden': 40,'Bank':45},
    'School': {'Post office': 59, 'Railway Station': 75},
    'Garden': {'Railway Station': 72},
    'Bank': {'Police Station': 60},
    'Police Station': {'University': 25},
    'Railway Station': {'University':40},
    'University': {}
}

# Heuristic values
heuristics = {
    'Home': 120, 'Bank': 80, 'Garden': 100,
    'School': 70, 'Railway Station': 20, 'Police Station': 26,'Post office':110,'University':0,
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

start, goal = 'Home', 'University'
path, cost = a_star_search(graph, heuristics, start, goal)

if path:
    print(f"Path found: {' -> '.join(path)}")
    print(f"Total cost: {cost}")
else:
    print("No path found.")
