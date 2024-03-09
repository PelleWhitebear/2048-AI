from src.game import game
from src.ai.ai import evaluate

import random

def expectimax(board, depth, maximizing_player):
    if depth == 0 or game.get_status(board) is not None:
        return evaluate(board)  # This should be your evaluation function

    if maximizing_player:
        # Implement the Max part of the Expectimax algorithm
        max_eval = float('-inf')
        for move in ["W", "A", "S", "D"]:
            new_board, _ = make_move(board, move)  # This should simulate the move
            eval = expectimax(new_board, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        # Implement the Average (Expectation) part of the Expectimax algorithm
        empty_positions = get_empty_positions(board)
        if not empty_positions:
            return evaluate_expect(board)  # Can't place a new tile, so just evaluate the board
        
        # Assume the probability of a '2' tile is 0.9 and a '4' tile is 0.1
        prob_2 = 0.9
        prob_4 = 0.1
        expected_value = 0
        
        for position in empty_positions:
            # Calculate the expected value for placing a '2'
            new_board = place_new_tile(board, position, 2)
            expected_value += prob_2 * expectimax(new_board, depth - 1, True)
            
            # Calculate the expected value for placing a '4'
            new_board = place_new_tile(board, position, 4)
            expected_value += prob_4 * expectimax(new_board, depth - 1, True)
            
        # Normalize the expected value by the number of possible placements
        return expected_value / (len(empty_positions) * (prob_2 + prob_4))

def make_move(board, move):
    # This should simulate the move and return the new board and a boolean indicating if the board changed
    return game.simulate_move(board, move)  # Make sure this function exists and correctly simulates moves

# Your evaluate function remains unchanged


def make_move(board, move):
    if move == "W":
        return game.move_up(board)
    elif move == "A":
        return game.move_left(board)
    elif move == "S":
        return game.move_down(board)
    elif move == "D":
        return game.move_right(board)

# Your evaluate function remains unchanged

def find_best_move(board, depth=3):
    best_score = float('-inf')
    best_move = None
    for move in ["W", "A", "S", "D"]:
        new_board, changed = make_move(board.copy(), move)  # Ensure board.copy() if necessary
        if changed:  # Only consider if the move changes the board
            score = expectimax(new_board, depth - 1, False)
            if score > best_score:
                best_score = score
                best_move = move
    return best_move


def evaluate_expect(board):
    w_open = 12
    w_edge = 5
    w_mono = -3.5
    w_merge = 4
    w_tile = 0
    w_empty = 1

    # Your existing evaluation components
    open_squares_bonus = sum(row.count(0) for row in board) * w_open
    edge_tiles_bonus = sum((board[i][j] + board[j][i]) * w_edge for i in [0, 3] for j in range(4))
    non_monotonic_penalty = sum((row[i] - row[i+1]) * w_mono for row in board for i in range(3))
    potential_merges_bonus = sum(board[i][j] * w_merge for i in range(4) for j in range(4) if (j < 3 and board[i][j] == board[i][j+1] and board[i][j] != 0) or (i < 3 and board[i][j] == board[i+1][j] and board[i][j] != 0))

    # Additional considerations
    tile_values = sum(sum(board[i][j] * w_tile[i][j] for j in range(4)) for i in range(4))
    empty_cells_bonus = sum(w_empty * board[i][j] for i in range(4) for j in range(4) if board[i][j] == 0)

    # Combine heuristics with adjustable weights
    score = (
        open_squares_bonus + edge_tiles_bonus + non_monotonic_penalty +
        potential_merges_bonus + tile_values + empty_cells_bonus
    )
    return score




import random

def get_empty_positions(board):
    empty_positions = []
    for row_index in range(len(board)):
        for column_index in range(len(board[row_index])):
            if board[row_index][column_index] == 0:
                empty_positions.append((row_index, column_index))
    return empty_positions

def place_new_tile(board, position, value):
    new_board = [row[:] for row in board]  # Make a deep copy of the board
    new_board[position[0]][position[1]] = value
    return new_board

