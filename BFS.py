from collections import deque
def bfs(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None
if __name__ == '__main__':
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2, 4],
        4: [3]
    }
    start_node = 0
    end_node = 4
    path = bfs(graph, start_node, end_node)
    if path :
        print(f"The shortest path between {start_node} and {end_node} is {path}")
    else:
        print(f"No path exists between {start_node} and {end_node}")
