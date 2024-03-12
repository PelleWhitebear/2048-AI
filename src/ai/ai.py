import numpy as np
from src.ai.weights import AIWeights
from src.game import game

def minimax(board, depth, maximizing_player):
    if depth == 0 or game.get_status(board):
        return evaluate(board)

    if maximizing_player:
        # Implement the Max part of the Minimax algorithm
        max_eval = float('-inf')
        for move in ["W", "A", "S", "D"]:
            new_board, _ = make_move(board, move)
            eval = minimax(new_board, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        # Implement the Min part of the Minimax algorithm
        min_eval = float('inf')
        for move in ["W", "A", "S", "D"]:
            new_board, _ = make_move(board, move)
            eval = minimax(new_board, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval
    


def make_move(board, move):
    if move == "W":
        return game.move_up(board)
    elif move == "A":
        return game.move_left(board)
    elif move == "S":
        return game.move_down(board)
    elif move == "D":
        return game.move_right(board)

def evaluate(board, ai_weights : AIWeights):
    open_squares_bonus = 0
    edge_tiles_bonus = 0
    non_monotonic_penalty = 0
    potential_merges_bonus = 0
    
    # Weights (These might need optimization)
    w_open = ai_weights.w_open
    w_edge = ai_weights.w_edge
    w_mono = ai_weights.w_mono
    w_merge = ai_weights.w_merge

    # Calculate open squares bonus
    open_squares_bonus = sum(row.count(0) for row in board) * w_open
    
    # Calculate edge tiles bonus (assuming highest value on edges is most beneficial)
    for i in [0, 3]:
        for j in range(4):
            edge_tiles_bonus += (board[i][j] + board[j][i]) * w_edge
    
    # Calculate potential merges bonus
    for i in range(4):
        for j in range(4):
            if j < 3 and board[i][j] == board[i][j+1] and board[i][j] != 0:
                potential_merges_bonus += board[i][j] * w_merge
            if i < 3 and board[i][j] == board[i+1][j] and board[i][j] != 0:
                potential_merges_bonus += board[i][j] * w_merge
    
    # Calculate non-monotonic penalty
    for row in board:
        for i in range(3):
            if row[i] > row[i+1] and row[i+1] != 0:
                non_monotonic_penalty += (row[i] - row[i+1]) * w_mono
    
    for col in zip(*board):
        for i in range(3):
            if col[i] > col[i+1] and col[i+1] != 0:
                non_monotonic_penalty += (col[i] - col[i+1]) * w_mono

    snake_score = snake_evaluation_function(board)

    # Combine heuristics to form a positional score
    score = open_squares_bonus + edge_tiles_bonus + non_monotonic_penalty + potential_merges_bonus + snake_score
    return score

def snake_evaluation_function(board):
    # Define a weight matrix that encourages a snake-like pattern starting from the bottom-right
    weights = np.array([
        [3,  2,  1,  0],
        [4,  5,  6,  7],
        [11, 10, 9,  8],
        [12, 13, 14, 15]
    ])
    
    # Convert the board to a numpy array for easier manipulation
    board_array = np.array(board)
    
    # Calculate the score by multiplying the board with the weight matrix
    score = np.sum(board_array * weights / 2)
    
    return score




def find_best_move(board, depth=3):
    best_score = float('-inf')
    best_move = None
    for move in ["W", "A", "S", "D"]:
        new_board, changed = make_move(board.copy(), move)  # Ensure board.copy() if necessary
        if changed:  # Only consider if the move changes the board
            score = minimax(new_board, depth - 1, False)
            if score > best_score:
                best_score = score
                best_move = move
    return best_move
