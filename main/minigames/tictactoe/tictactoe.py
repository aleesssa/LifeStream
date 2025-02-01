# Define the board and the players
board = [" " for _ in range(9)]
human = "X"
computer = "O"

# Check for a win
def check_winner(board, player):
    win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                    (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                    (0, 4, 8), (2, 4, 6)]
    return any(board[i] == board[j] == board[k] == player for i, j, k in win_patterns)

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, computer):
        return 1
    elif check_winner(board, human):
        return -1
    elif " " not in board:
        return 0

    if is_maximizing:
        best = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = computer
                best = max(best, minimax(board, depth + 1, False))
                board[i] = " "
        return best
    else:
        best = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = human
                best = min(best, minimax(board, depth + 1, True))
                board[i] = " "
        return best

# AI Move
def best_move(board):
    best_val = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = computer
            move_val = minimax(board, 0, False)
            board[i] = " "
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

# Display the board
def print_board(board):
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))
        if i < 6:
            print("-" * 5)

# Main game loop
def play_game():
    while " " in board:
        # Human's turn
        print_board(board)
        move = int(input("Enter your move (0-8): "))
        if board[move] == " ":
            board[move] = human
        else:
            print("Invalid move!")
            continue
        
        if check_winner(board, human):
            print_board(board)
            print("You win!")
            break
        
        # Computer's turn
        if " " in board:
            move = best_move(board)
            board[move] = computer
            if check_winner(board, computer):
                print_board(board)
                print("Computer wins! You won't be getting any hints for now.")
                break
        else:
            print_board(board)
            print("It's a tie!")
            break

play_game()
