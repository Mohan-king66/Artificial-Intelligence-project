def alphabeta(node, depth, alpha, beta, maximizing, values):
    if depth == 0 or node >= len(values):
        return values[node]
    if maximizing:
        value = float('-inf')
        for i in range(2):
            value = max(value, alphabeta(node*2+i+1, depth-1, alpha, beta, False, values))
            alpha = max(alpha, value)
            if alpha >= beta: break
        return value
    else:
        value = float('inf')
        for i in range(2):
            value = min(value, alphabeta(node*2+i+1, depth-1, alpha, beta, True, values))
            beta = min(beta, value)
            if alpha >= beta: break
        return value

values = [3, 5, 6, 9, 1, 2, 0, -1]  # leaf node values
print("Optimal value:", alphabeta(0, 3, float('-inf'), float('inf'), True, values))
