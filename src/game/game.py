import random


def start_game():
    board = [[0] * 4 for i in range(4)]

    add_tile(board)
    add_tile(board)

    return board


def add_tile(board):
    r = random.randint(0, 3)
    c = random.randint(0, 3)

    while board[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    # 90% chance of getting a 2, 10% chance of getting a 4
    board[r][c] = 2 if random.random() < 0.9 else 4


def get_status(board):
    # Check for the win condition if needed
    # for i in range(4):
    #     for j in range(4):
    #         if board[i][j] == 2048:
    #             return 'W'

    # Check for any possible moves left
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:  # Check for empty cell
                return False
            if i < 3 and board[i][j] == board[i + 1][j]:  # Check for vertical merge
                return False
            if j < 3 and board[i][j] == board[i][j + 1]:  # Check for horizontal merge
                return False

    # No moves left, game over
    return True




def move_up(board):
    new_board = [[0] * 4 for _ in range(4)]
    changed = False

    for j in range(4):
        p = 0

        for i in range(4):
            if board[i][j] != 0:
                if new_board[p][j] == 0:
                    new_board[p][j] = board[i][j]
                elif new_board[p][j] == board[i][j]:
                    new_board[p][j] *= 2
                    p += 1
                    changed = True
                else:
                    p += 1
                    new_board[p][j] = board[i][j]

                if i != p:
                    changed = True

    return new_board, changed


def move_down(board):
    new_board = [[0]*4 for _ in range(4)]
    changed = False

    for j in range(4):
        position = 3

        for i in range(3, -1, -1):
            if board[i][j] != 0:
                if new_board[position][j] == 0:
                    new_board[position][j] = board[i][j]
                elif new_board[position][j] == board[i][j]:
                    new_board[position][j] *= 2
                    position -= 1
                    changed = True
                else:
                    position -= 1
                    new_board[position][j] = board[i][j]

                if i != position:
                    changed = True

    return new_board, changed


def move_left(board):
    new_board = [[0]*4 for _ in range(4)]
    changed = False

    for i in range(4):
        position = 0

        for j in range(4):
            if board[i][j] != 0:
                if new_board[i][position] == 0:
                    new_board[i][position] = board[i][j]
                elif new_board[i][position] == board[i][j]:
                    new_board[i][position] *= 2
                    position += 1
                    changed = True
                else:
                    position += 1
                    new_board[i][position] = board[i][j]

                if j != position:
                    changed = True

    return new_board, changed


def move_right(board):
    new_board = [[0]*4 for _ in range(4)]
    changed = False

    for i in range(4):
        position = 3

        for j in range(3, -1, -1):
            if board[i][j] != 0:
                if new_board[i][position] == 0:
                    new_board[i][position] = board[i][j]
                elif new_board[i][position] == board[i][j]:
                    new_board[i][position] *= 2
                    position -= 1
                    changed = True
                else:
                    position -= 1
                    new_board[i][position] = board[i][j]

                if j != position:
                    changed = True

    return new_board, changed