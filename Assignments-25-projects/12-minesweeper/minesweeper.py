import random


class Minesweeper:
    def __init__(self, rows, cols, num_mines):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.revealed = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.mines = set()
        self.game_over = False
        
     
        self.place_mines()
        
    def place_mines(self):
        while len(self.mines) < self.num_mines:
            mine_pos = (random.randint(0, self.rows - 1), random.randint(0, self.cols - 1))
            self.mines.add(mine_pos)
    
    def display_board(self):
        print("  " + " ".join([str(i) for i in range(self.cols)]))
        for r in range(self.rows):
            print(f"{r} " + " ".join(self.revealed[r]))
        print()

    def count_adjacent_mines(self, row, col):
        count = 0
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if 0 <= r < self.rows and 0 <= c < self.cols and (r, c) in self.mines:
                    count += 1
        return count

    def reveal_cell(self, row, col):
        if self.revealed[row][col] != ' ':
            return
        
        # Reveal the cell
        self.revealed[row][col] = str(self.count_adjacent_mines(row, col)) if (row, col) not in self.mines else '*'

      
        if self.revealed[row][col] == '0':
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if 0 <= r < self.rows and 0 <= c < self.cols and self.revealed[r][c] == ' ':
                        self.reveal_cell(r, c)

    def play(self):
        while not self.game_over:
            self.display_board()
            
      
            try:
                row, col = map(int, input("Enter row and column (separated by space): ").split())
                if not (0 <= row < self.rows and 0 <= col < self.cols):
                    print("Invalid input! Please enter row and column within bounds.")
                    continue
            except ValueError:
                print("Invalid input! Please enter numbers separated by space.")
                continue
            
            if (row, col) in self.mines:
                self.game_over = True
                self.revealed[row][col] = '*'
                print("Game Over! You hit a mine!")
                self.display_board()
            else:
                self.reveal_cell(row, col)
                
         
            if self.check_win():
                self.game_over = True
                print("Congratulations! You've won the game!")
                self.display_board()

    def check_win(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.revealed[r][c] == ' ' and (r, c) not in self.mines:
                    return False
        return True


def start_game():
    print("Welcome to Minesweeper!")

    rows = 5
    cols = 5
    num_mines = 5
    game = Minesweeper(rows, cols, num_mines)
    
    game.play()


if __name__ == "__main__":
    start_game()
