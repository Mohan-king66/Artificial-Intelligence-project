board = [' ' for _ in range(9)]
def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False
def tic_tac_toe():
    current_player = 'X'
    for turn in range(9):
        display_board()
        move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
        if board[move] != ' ':
            print("Position already taken. Try again.")
            continue
        board[move] = current_player
        if check_winner(current_player):
            display_board()
            print(f" Player {current_player} wins!")
            return
        current_player = 'O' if current_player == 'X' else 'X'
    display_board()
    print("It's a tie!")
tic_tac_toe()
