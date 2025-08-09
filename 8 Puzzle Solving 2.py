from collections import deque
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def find_zero(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j
def copy(puzzle):
    return [row[:] for row in puzzle]
def to_string(puzzle):
    return ''.join(str(num) for row in puzzle for num in row)
def get_neighbors(puzzle):
    x, y = find_zero(puzzle)
    neighbors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_puzzle = copy(puzzle)
            new_puzzle[x][y], new_puzzle[nx][ny] = new_puzzle[nx][ny], new_puzzle[x][y]
            neighbors.append(new_puzzle)
    return neighbors
def solve(start):
    queue = deque()
    visited = set()
    queue.append((start, []))
    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path + [current]
        key = to_string(current)
        if key in visited:
            continue
        visited.add(key)
        for neighbor in get_neighbors(current):
            queue.append((neighbor, path + [current]))
    return None
def show(steps):
    for step in steps:
        for row in step:
            print(row)
        print()
start = [
    [1, 2, 3],
    [5, 0, 6],
    [4, 7, 8]
]
solution = solve(start)
if solution:
    print("Steps to solve the puzzle:")
    show(solution)
else:
    print("No solution found.")
