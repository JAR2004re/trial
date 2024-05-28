class TicTacToe:
    def __init__(self):
        self.board = [[' ']*3 for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.check_winner(row, col)
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        else:
            print("Invalid move! Try again.")
            return False
    def check_winner(self, row, col):
        if self.board[row][0] == self.board[row][1] == self.board[row][2] != ' ':
            self.winner = self.board[row][0]
        elif self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
            self.winner = self.board[0][col]
        elif (row == col and self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ') or \
             (row + col == 2 and self.board[0][2] == self.board[1][1] == self.board[2][0] != ' '):
            self.winner = self.board[1][1]
    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True
    def game_over(self):
        return self.winner is not None or self.is_board_full()
def main():
    game = TicTacToe()
    while not game.game_over():
        game.print_board()
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))
        if game.make_move(row, col):
            if game.winner:
                print(f"Player {game.winner} wins!")
            elif game.is_board_full():
                print("It's a draw!")
            else:
                print(f"Player {game.current_player}'s turn.")
    game.print_board()
if __name__ == "__main__":
    main()