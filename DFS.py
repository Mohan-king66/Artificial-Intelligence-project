def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}
visited = set()
start_node = 0
print("The Depth First Search Traversal for The Graph is as Follows:")
dfs(graph, start_node, visited)
