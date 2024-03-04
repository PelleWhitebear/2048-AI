from src.game import game

class Game:
    def __init__(self, ai=False):
        self.board = game.start_game()
        self.ai = ai
        self.print_board()

    def print_board(self):
        for row in self.board:
            print(row)

    def play(self, direction):
        changed = False
        if direction.upper() == 'W':
            self.board, changed = game.move_up(self.board)
        elif direction.upper() == 'S':
            self.board, changed = game.move_down(self.board)
        elif direction.upper() == 'A':
            self.board, changed = game.move_left(self.board)
        elif direction.upper() == 'D':
            self.board, changed = game.move_right(self.board)
        else:
            print("Invalid")
            return

        if changed:
            game.add_tile(self.board)

        status = game.get_status(self.board)

        if status == 'W':
            print("You win!")
            self.print_board()
            return True
        elif status == 'L':
            print("Game over")
            self.print_board()
            return True

        self.print_board()
        return False