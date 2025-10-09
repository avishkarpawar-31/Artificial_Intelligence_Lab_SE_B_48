maze = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', ' ', ' ', '#', 'E', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]
def find_points(maze):
    start = end = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)
    return start, end
from collections import deque

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if maze[nx][ny] in (' ', 'E') and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + [(nx, ny)]))
    return None

def dfs(maze, start, end):
    stack = [(start, [start])]
    visited = set()

    while stack:
        (x, y), path = stack.pop()
        if (x, y) == end:
            return path
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                if maze[nx][ny] in (' ', 'E'):
                    stack.append(((nx, ny), path + [(nx, ny)]))
    return None
def print_maze_with_path(maze, path):
    maze_copy = [row[:] for row in maze]
    for x, y in path:
        if maze_copy[x][y] not in ('S', 'E'):
            maze_copy[x][y] = '*'
    for row in maze_copy:
        print(''.join(row))
maze = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', ' ', ' ', '#', 'E', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]

start, end = find_points(maze)

# Run BFS
bfs_path = bfs(maze, start, end)
print("BFS Path:")
print_maze_with_path(maze, bfs_path)

print("\n")

# Run DFS
dfs_path = dfs(maze, start, end)
print("DFS Path:")
print_maze_with_path(maze, dfs_path)

