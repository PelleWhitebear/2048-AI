from src.ai import ai_expect as ai
from src.ai import ai_montecarlo as MCTS
from src.game import game

class Game:
    def __init__(self, ai=False, ai_choice : int = 1):
        self.board = game.start_game()
        self.ai = ai
        self.ai_choice = ai_choice
        self.print_board()

    def print_board(self):
        for row in self.board:
            print(row)
        print("\n")

    def ai_move(self):
        if self.ai_choice == 1:
            best_move = ai.find_best_move(self.board, depth=5)
        elif self.ai_choice == 2:
            best_move = MCTS.find_best_move(self.board, iterations=1)
        self.play(best_move)

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
          #  self.print_board()
          #  return True
        elif status == 'L':
            print("Game over")
            self.print_board()
            return True

        self.print_board()
        return False