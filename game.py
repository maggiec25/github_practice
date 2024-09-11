def print_board(board):
    print("\n".join([" | ".join(row) for row in board]))
    print()

def check_winner(board, player):
    win_conditions = [
        # Rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    
    while True:
        print(f"Player {current_player}'s turn")
        
        while True:
            try:
                row = int(input("Enter the row (0, 1, or 2): "))
                col = int(input("Enter the column (0, 1, or 2): "))
                if board[row][col] == ' ':
                    board[row][col] = current_player
                    break
                else:
                    print("Cell already taken, try again.")
            except (IndexError, ValueError):
                print("Invalid input, please enter numbers between 0 and 2.")
        
        print_board(board)
        
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        
        if is_board_full(board):
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()