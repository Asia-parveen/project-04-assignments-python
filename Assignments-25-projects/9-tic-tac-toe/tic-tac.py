import time
import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def is_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe! 🏆")
    time.sleep(1)
    
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    
    current_player = 0  # Index for players list
    
    while True:
        print_board(board)
        
        try:
            row = int(input(f"Player {players[current_player]}, enter row (0-2): "))
            col = int(input(f"Player {players[current_player]}, enter column (0-2): "))
        except ValueError:
            print("Invalid input! Please enter numbers between 0 and 2.")
            continue
        
        if row not in range(3) or col not in range(3) or board[row][col] != " ":
            print("Invalid move! Try again.")
            continue
        
        board[row][col] = players[current_player]
        
        # Check winner
        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"🎉 Player {players[current_player]} wins! 🎉")
            break
        
        # Check if board is full
        if is_full(board):
            print_board(board)
            print("It's a tie! 🤝")
            break
        
        # Switch player
        current_player = 1 - current_player  # Toggle between 0 and 1
        
        time.sleep(0.5)  # Small delay for better UX

if __name__ == "__main__":
    tic_tac_toe()