import heapq
def astar(start, goal, neighbors_fn, heuristic_fn):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    while frontier:
        _, current = heapq.heappop(frontier)
        if current == goal:
            break
        for neighbor in neighbors_fn(current):
            new_cost = cost_so_far[current] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic_fn(neighbor, goal)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path, cost_so_far.get(goal, float('inf'))
def neighbors(node):
    x, y = node
    moves = [(0,1), (1,0), (0,-1), (-1,0)]
    result = []
    for dx, dy in moves:
        nxt = (x+dx, y+dy)
        if 0 <= nxt[0] < 5 and 0 <= nxt[1] < 5:  # 5x5 grid
            result.append(nxt)
    return result
def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
start = (0, 0)
goal = (4, 4)
path, cost = astar(start, goal, neighbors, heuristic)
print("Path:", path)
print("Cost:", cost)
