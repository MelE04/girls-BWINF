def read_file(filename):
    with open(filename, "r") as text:
        dimensions = text.readline().strip().split()
        lines = int(dimensions[0])
        columns = int(dimensions[1])

        quadratien = []
        kassiopeia = None

        for row_index in range(lines):
            line = text.readline().rstrip("\n")
            row = list(line)
            if 'K' in row:
                kassiopeia = (row_index, row.index('K'))  # (row, col)
            quadratien.append(row)

        return quadratien, kassiopeia

# Directions: N, S, W, E
DIRS = {
    'N': (-1, 0),
    'S': (1, 0),
    'W': (0, -1),
    'O': (0, 1),
}

def count_reachable_spaces(grid):
    return sum(row.count(' ') for row in grid)

def is_valid(x, y, grid, visited):
    return (0 <= x < len(grid)) and (0 <= y < len(grid[0])) and grid[x][y] == ' ' and not visited[x][y]

def dfs_all(field, grid, visited):
    x, y = field
    if visited[x][y]:
        return
    visited[x][y] = True
    for dx, dy in DIRS.values():
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, grid, visited):
            dfs_all((nx, ny), grid, visited)

def dfs_path(x, y, grid, visited, path, total_white, step=0):
    if step == total_white:
        return True  # success: visited all white tiles exactly once

    for dir_letter, (dx, dy) in DIRS.items():
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, grid, visited):
            visited[nx][ny] = True
            path.append(dir_letter)
            if dfs_path(nx, ny, grid, visited, path, total_white, step + 1):
                return True
            path.pop()
            visited[nx][ny] = False
    return False

# === Main ===
file = input("Dateiname: ")
grid, kassiopeia = read_file(file)

if kassiopeia is None:
    print("Kassiopeia not found.")
    exit(1)

# 1. Check if all white tiles are reachable
reachable_white = count_reachable_spaces(grid)
visited = [[False for _ in row] for row in grid]
dfs_all(kassiopeia, grid, visited)

visited_count = sum(
    1 for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == ' ' and visited[i][j]
)

if visited_count == reachable_white:
    print("Ja")
else:
    print("Nein")

# 2. Try to find a path visiting each white tile exactly once
visited_once = [[False for _ in row] for row in grid]
x0, y0 = kassiopeia
path = []

# Important: do NOT count K's cell unless it's a space
start_is_space = grid[x0][y0] == ' '
if start_is_space:
    visited_once[x0][y0] = True
    total_steps = reachable_white - 1
else:
    total_steps = reachable_white

if dfs_path(x0, y0, grid, visited_once, path, total_steps):
    print(" ".join(path))