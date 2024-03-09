from src.game import game
from src.ai.ai import evaluate
import random
import numpy as np

class Node:
    def __init__(self, board, parent=None):
        self.board = board
        self.parent = parent
        self.children = []
        self.visits = 0
        self.score = 0

def expand_node(node):
    for move in ["W", "A", "S", "D"]:
        new_board, changed = make_move(node.board.copy(), move)
        if changed:
            child_node = Node(new_board, parent=node)
            node.children.append(child_node)

def rollout(node):
    board = node.board.copy()
    while not game.get_status(board):
        move = random.choice(["W", "A", "S", "D"])
        board, _ = make_move(board, move)
    return evaluate(board)

def backpropagate(node, score):
    while node is not None:
        node.visits += 1
        node.score += score
        node = node.parent

def ucb1(node, parent_visits):
    if node.visits == 0:
        return float('inf')
    return (node.score / node.visits) + (2 * (np.log(parent_visits) / node.visits) ** 0.5)

def mcts_search(board, iterations):
    root = Node(board)
    for _ in range(iterations):
        node = root
        while node.children:
            parent_visits = sum(child.visits for child in node.children)
            node = max(node.children, key=lambda x: ucb1(x, parent_visits))
        if node.visits == 0:
            expand_node(node)
        rollout_score = rollout(node)
        backpropagate(node, rollout_score)
    best_move = max(root.children, key=lambda x: x.score / x.visits)
    return best_move.board


def make_move(board, move):
    if move == "W":
        return game.move_up(board)
    elif move == "A":
        return game.move_left(board)
    elif move == "S":
        return game.move_down(board)
    elif move == "D":
        return game.move_right(board)

def find_best_move(board, iterations=100):
    new_board = mcts_search(board.copy(), iterations)
    if new_board is None:
        return None
    else:
        return find_changed_move(board, new_board)

def find_changed_move(old_board, new_board):
    for move in ["W", "A", "S", "D"]:
        if make_move(old_board.copy(), move)[1] == new_board:
            return move




