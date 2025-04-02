# Tic-Tac-Toe AI Python Project

import random

# Initializing the board
board = [' ' for _ in range(9)]  # A list of 9 spaces for the board

# Constants for easy comparison
PLAYER = 'X'
COMPUTER = 'O'

# Function to print the board
def print_board():
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}\n")

# Check if a player has won
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Check if the board is full
def is_board_full():
    return ' ' not in board

# Minimax Algorithm
def minimax(depth, is_maximizing):
    if check_winner(COMPUTER):
        return 1
    if check_winner(PLAYER):
        return -1
    if is_board_full():
        return 0

    if is_maximizing:
        best = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = COMPUTER
                best = max(best, minimax(depth + 1, False))
                board[i] = ' '
        return best
    else:
        best = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = PLAYER
                best = min(best, minimax(depth + 1, True))
                board[i] = ' '
        return best

# Function to get the computer's best move
def get_computer_move():
    best_val = -float('inf')
    best_move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = COMPUTER
            move_val = minimax(0, False)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                best_move = i
    return best_move

# Player's move
def player_move():
    while True:
        try:
            move = int(input("Player, enter your move (0-8): "))
            if move < 0 or move > 8:
                print("Invalid move! Please enter a number between 0 and 8.")
            elif board[move] != ' ':
                print("This cell is already taken!")
            else:
                board[move] = PLAYER
                break
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 8.")

# Game loop
def play_game():
    print("Welcome to Tic-Tac-Toe AI!")
    print_board()

    while True:
        # Player's turn
        player_move()
        print_board()
        if check_winner(PLAYER):
            print("Player wins!")
            break
        if is_board_full():
            print("It's a tie!")
            break

        # Computer's turn
        print("Computer's turn...")
        move = get_computer_move()
        board[move] = COMPUTER
        print_board()
        if check_winner(COMPUTER):
            print("Computer wins!")
            break
        if is_board_full():
            print("It's a tie!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
