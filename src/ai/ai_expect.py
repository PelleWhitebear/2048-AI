from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from src.game import game
from src.ai.ai import evaluate
from src.ai.weights import AIWeights

import random

def expectimax(board, depth, maximizing_player, ai_weights: AIWeights, alpha=float('-inf'), beta=float('inf')):
    game_status = game.get_status(board)
    if depth == 0 or game_status:
        return evaluate(board, ai_weights)  # Your evaluation function

    if maximizing_player:
        max_eval = float('-inf')
        for move in ["W", "A", "S", "D"]:
            new_board, _ = make_move(board, move)
            eval = expectimax(new_board, depth - 1, False, ai_weights, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Prune remaining branches
        return max_eval
    else:
        empty_positions = get_empty_positions(board)
        if not empty_positions:
            return evaluate(board, ai_weights)

        prob_2 = 0.9
        prob_4 = 0.1
        expected_value = 0

        for position in empty_positions:
            new_board_2 = place_new_tile(board, position, 2)
            eval_2 = expectimax(new_board_2, depth - 1, True, ai_weights, alpha, beta)
            expected_value += prob_2 * eval_2

            new_board_4 = place_new_tile(board, position, 4)
            eval_4 = expectimax(new_board_4, depth - 1, True, ai_weights, alpha, beta)
            expected_value += prob_4 * eval_4

            alpha = max(alpha, eval_2, eval_4)
            if beta <= alpha:
                break  # Prune remaining branches

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

def find_best_move(board, depth, ai_weights : AIWeights):
    best_score = float('-inf')
    best_move = None

    # Iterate through each possible move
    for move in ["W", "A", "S", "D"]:
        # Attempt to make the move on a copy of the board
        new_board, changed = make_move(board.copy(), move)

        # If the move changes the board, evaluate it using expectimax
        if changed:
            score = expectimax(new_board, depth - 1, False, ai_weights)
            # score = expectimax_alpha_beta_multiprocess(new_board, depth - 1, False, ai_weights)
            # score = expectimax_alpha_beta_multiprocess(new_board, depth - 1, False, ai_weights)
            # Update the best score and move if this move is better
            if score > best_score:
                best_score = score
                best_move = move

    # If best_move is None, it means no move improved the board, which might indicate a game over scenario
    #if best_move is None:
        #print("No valid moves available. Game may be over or in a deadlocked state.")

    return best_move



def evaluate_expect(board, ai_weights : AIWeights):
    w_open = ai_weights.w_open
    w_edge = ai_weights.w_edge
    w_mono = ai_weights.w_mono
    w_merge = ai_weights.w_merge
    w_empty = ai_weights.w_empty

    w_tile = [
    [1, 2, 4, 8],
    [2, 4, 8, 16],
    [4, 8, 16, 32],
    [8, 16, 32, 64]
]

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

# --------------------------------------------------------------------------------------------

def evaluate_worker(board, ai_weights):
    return evaluate_expect(board, ai_weights)

def expectimax_parallel(board, depth, maximizing_player, ai_weights, alpha=float('-inf'), beta=float('inf')):
    game_status = game.get_status(board)
    if depth == 0 or game_status:
        return evaluate_expect(board, ai_weights)

    if maximizing_player:
        max_eval = float('-inf')
        for move in ["W", "A", "S", "D"]:
            new_board, _ = make_move(board, move)
            eval = expectimax(new_board, depth - 1, False, ai_weights, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Prune remaining branches
        return max_eval

    else:
        empty_positions = get_empty_positions(board)
        if not empty_positions:
            return evaluate_expect(board, ai_weights)

        prob_2 = 0.9
        prob_4 = 0.1
        expected_value = 0

        with ProcessPoolExecutor() as executor:
            futures = []
            for position in empty_positions:
                new_board_2 = place_new_tile(board, position, 2)
                future_2 = executor.submit(evaluate_worker, new_board_2, ai_weights)
                futures.append(future_2)

                new_board_4 = place_new_tile(board, position, 4)
                future_4 = executor.submit(evaluate_worker, new_board_4, ai_weights)
                futures.append(future_4)

            for future in futures:
                eval_result = future.result()
                expected_value += prob_2 * eval_result if future in futures[:len(futures) // 2] else prob_4 * eval_result

        return expected_value / (len(empty_positions) * (prob_2 + prob_4))