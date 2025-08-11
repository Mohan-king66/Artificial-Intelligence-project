def evaluate(state):
    if check_winner(state, "X"):
        return 10
    elif check_winner(state, "O"):
        return -10
    else:
        return 0
def game_over(state):
    return check_winner(state, "X") or check_winner(state, "O") or not any(cell == " " for cell in state)
def get_possible_moves(state):
    return [i for i, cell in enumerate(state) if cell == " "]
def make_move(state, move, player):
    new_state = state[:]
    new_state[move] = player
    return new_state
def check_winner(state, player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]             
    ]
    return any(all(state[pos] == player for pos in combo) for combo in win_positions)
def alpha_beta_pruning(state, depth, alpha, beta, player):
    if depth == 0 or game_over(state):
        return evaluate(state), None
    if player == "X":  # Maximizing
        best_score = float('-inf')
        best_move = None
        for move in get_possible_moves(state):
            new_state = make_move(state, move, player)
            score, _ = alpha_beta_pruning(new_state, depth - 1, alpha, beta, "O")
            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score, best_move
    else:  
        best_score = float('inf')
        best_move = None
        for move in get_possible_moves(state):
            new_state = make_move(state, move, player)
            score, _ = alpha_beta_pruning(new_state, depth - 1, alpha, beta, "X")
            if score < best_score:
                best_score = score
                best_move = move
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score, best_move
if __name__ == "__main__":
    initial_state = ["X", "X", " ",
                     "O", "O", " ",
                     " ", " ", " "]
    score, move = alpha_beta_pruning(initial_state, depth=9, alpha=float('-inf'), beta=float('inf'), player="X")
    print("Best evaluated score for X:", score)
    print("Best move for X:", move)
