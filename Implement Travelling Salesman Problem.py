from itertools import permutations
nodes = ['A', 'F', 'G', 'I', 'J']
graph = [
    [0,  2,  9, 10, 0],  
    [1,  0,  6,  4, 5],  
    [15, 7,  0,  8, 9],  
    [6,  3, 12, 0, 14],  
    [7, 11, 5, 13, 0]    
]
def tsp(graph, start=0):
    n = len(graph)
    cities = list(range(n))
    min_distance = float('inf')
    best_route = []
    for perm in permutations(cities):
        if perm[0] != start:
            continue
        dist = 0
        for i in range(n - 1):
            dist += graph[perm[i]][perm[i+1]]
        dist += graph[perm[-1]][perm[0]]  
        if dist < min_distance:
            min_distance = dist
            best_route = perm
    return min_distance, best_route
distance, route = tsp(graph)
named_route = [nodes[i] for i in route]
print("Shortest Distance:", distance)
print("Path found:", named_route)
