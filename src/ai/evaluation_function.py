import numpy as np
from src.ai.weights import AIWeights

def evaluate(board, ai_weights : AIWeights):
    open_squares_bonus = 0
    edge_tiles_bonus = 0
    non_monotonic_penalty = 0
    potential_merges_bonus = 0
    matrix_score = 0
    
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

    if (ai_weights.SnakeMatrix):
        matrx_score = snake_evaluation_function(board, ai_weights.w_empty)
    else:
        matrix_score = increase_towards_left_corner_matrix(board, ai_weights.w_empty)

    # Combine heuristics to form a positional score
    score = open_squares_bonus + edge_tiles_bonus + non_monotonic_penalty + potential_merges_bonus + matrx_score
    return score

def snake_evaluation_function(board, w_snake):
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
    score = np.sum(board_array * weights * w_snake)
    
    return score

def increase_towards_left_corner_matrix(board, w_matrix):

    weights = np.array([
    [1, 2, 4, 8],
    [2, 4, 8, 16],
    [4, 8, 16, 32],
    [8, 16, 32, 64]
    ])


    
    # Convert the board to a numpy array for easier manipulation
    board_array = np.array(board)
    
    # Calculate the score by multiplying the board with the weight matrix
    score = np.sum(board_array * weights * w_matrix)





