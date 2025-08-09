import heapq
def a_star(graph, start, goal, h):
    open_list = [(h[start], start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = h[start]
    closed_list = set()

    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        closed_list.add(current)
        for neighbor, cost in graph[current].items():
            if neighbor in closed_list:
                continue
            tentative_g = g_score[current] + cost
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + h[neighbor]
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None
