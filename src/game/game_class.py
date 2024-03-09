from src.ai.weights import AIWeights
from src.ai import ai_expect as ai
from src.ai import ai_montecarlo as MCTS
from src.game import game

class Game:
    def __init__(self, ai=False, ai_choice : int = 1):
        self.board = game.start_game()
        self.ai = ai
        self.ai_choice = ai_choice
        #self.print_board()

    def print_board(self):
        for row in self.board:
            print(row)
        print("\n")

    def ai_move(self, ai_weights : AIWeights):
        best_move = None
        if self.ai_choice == 1:
            best_move = ai.find_best_move(self.board, depth=5, ai_weights=ai_weights)
        elif self.ai_choice == 2:
            best_move = MCTS.find_best_move(self.board, iterations=1)

        # If best_move is None, no valid move was found
        if best_move is None:
            # Handle no valid move found; could be an indication the game is over
            # For example, you can print a message, choose a random move, or end the game
           # print("No valid moves found by AI.")
            return False, getMaxValue(self.board)

        return self.play(best_move)


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
           # print("!!!!!!!!!!!! Invalid")
            return False, getMaxValue(self.board)

        if changed:
            game.add_tile(self.board)
            self.print_board()
            return True, getMaxValue(self.board)
        
        self.print_board()
        return game.get_status(self.board), getMaxValue(self.board)

     

def getMaxValue(board) -> int:
    max = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] > max:
                max = board[i][j]
    return int(max)