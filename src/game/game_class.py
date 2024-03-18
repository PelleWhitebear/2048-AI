from src.ai.weights import AIWeights
from src.ai import ai_expect as ai
from src.game import game

class Game:
    def __init__(self, ai=False, print_board_bool=True, ai_search_depth : int = 3):
        self.board = game.start_game()
        self.ai = ai
        self.print_board_bool = print_board_bool
        self.search_depth = ai_search_depth

        #self.print_board()

    def print_board(self):
       if (self.print_board_bool):
        for row in self.board:
            print(row)
        print("\n")

    def ai_move(self, ai_weights : AIWeights):
        best_move = None
        best_move = ai.find_best_move(self.board, depth=self.search_depth, ai_weights=ai_weights)

        # If best_move is None, no valid move was found
        if best_move is None:
            # Handle no valid move found; could be an indication the game is over
            # For example, you can print a message, choose a random move, or end the game
           # print("No valid moves found by AI.")
            highest_tile, highest_sum = getMaxValue(self.board)
            return False, highest_tile, highest_sum

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
            highest_tile, highest_sum = getMaxValue(self.board)
            return False, highest_tile, highest_sum

        if changed:
            game.add_tile(self.board)
            self.print_board()
            highest_tile, highest_sum = getMaxValue(self.board)
            return True, highest_tile, highest_sum
        
        self.print_board()
        highest_tile, highest_sum = getMaxValue(self.board)

        return game.get_status(self.board), highest_tile, highest_sum

     

def getMaxValue(board):
    max = 0
    sum = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] > max:
                max = board[i][j]
            sum += board[i][j]
    return int(max), int(sum)