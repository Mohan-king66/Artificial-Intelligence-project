map_graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []  
}
colors = ['Red', 'Green', 'Blue']
def is_consistent(assignment, country, color):
    for neighbor in map_graph[country]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True
def backtrack(assignment):
    if len(assignment) == len(map_graph):
        return assignment
    unassigned = [c for c in map_graph if c not in assignment]
    country = unassigned[0]
    for color in colors:
        if is_consistent(assignment, country, color):
            assignment[country] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[country] 
    return None  
solution = backtrack({})
if solution:
    print("Map Coloring Solution:")
    for country in sorted(solution):
        print(f"{country}: {solution[country]}")
else:
    print("No solution found.")
