import math
import random
from copy import deepcopy

# -----------------------------
# TIC TAC TOE GAME
# -----------------------------

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False

    def undo_move(self, position):
        self.board[position] = ' '

    def winner(self):
        wins = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]

        for combo in wins:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return self.board[a]

        if ' ' not in self.board:
            return 'Draw'

        return None

    def print_board(self):
        for i in range(0, 9, 3):
            print(self.board[i:i+3])
        print()


# -----------------------------
# MINIMAX
# -----------------------------

def minimax(game, depth, maximizing):
    result = game.winner()

    if result == 'X':
        return 1
    elif result == 'O':
        return -1
    elif result == 'Draw':
        return 0

    if maximizing:
        best = -math.inf

        for move in game.available_moves():
            game.make_move(move, 'X')
            score = minimax(game, depth + 1, False)
            game.undo_move(move)

            best = max(best, score)

        return best

    else:
        best = math.inf

        for move in game.available_moves():
            game.make_move(move, 'O')
            score = minimax(game, depth + 1, True)
            game.undo_move(move)

            best = min(best, score)

        return best


# -----------------------------
# ALPHA BETA PRUNING
# -----------------------------

def alpha_beta(game, depth, alpha, beta, maximizing):
    result = game.winner()

    if result == 'X':
        return 1
    elif result == 'O':
        return -1
    elif result == 'Draw':
        return 0

    if maximizing:
        value = -math.inf

        for move in game.available_moves():
            game.make_move(move, 'X')

            value = max(value,
                        alpha_beta(game, depth+1, alpha, beta, False))

            game.undo_move(move)

            alpha = max(alpha, value)

            if beta <= alpha:
                break

        return value

    else:
        value = math.inf

        for move in game.available_moves():
            game.make_move(move, 'O')

            value = min(value,
                        alpha_beta(game, depth+1, alpha, beta, True))

            game.undo_move(move)

            beta = min(beta, value)

            if beta <= alpha:
                break

        return value


# -----------------------------
# HEURISTIC FUNCTION
# -----------------------------

def heuristic(game):
    score = 0

    lines = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for line in lines:
        values = [game.board[i] for i in line]

        if values.count('X') == 2 and values.count(' ') == 1:
            score += 5

        if values.count('O') == 2 and values.count(' ') == 1:
            score -= 5

    return score


# -----------------------------
# HEURISTIC ALPHA BETA
# -----------------------------

def heuristic_alpha_beta(game, depth, alpha, beta, maximizing):

    result = game.winner()

    if result == 'X':
        return 100
    elif result == 'O':
        return -100
    elif result == 'Draw':
        return 0

    if depth == 0:
        return heuristic(game)

    if maximizing:
        value = -math.inf

        for move in game.available_moves():
            game.make_move(move, 'X')

            value = max(value,
                        heuristic_alpha_beta(
                            game,
                            depth-1,
                            alpha,
                            beta,
                            False
                        ))

            game.undo_move(move)

            alpha = max(alpha, value)

            if beta <= alpha:
                break

        return value

    else:
        value = math.inf

        for move in game.available_moves():
            game.make_move(move, 'O')

            value = min(value,
                        heuristic_alpha_beta(
                            game,
                            depth-1,
                            alpha,
                            beta,
                            True
                        ))

            game.undo_move(move)

            beta = min(beta, value)

            if beta <= alpha:
                break

        return value


# -----------------------------
# MONTE CARLO TREE SEARCH
# -----------------------------

def random_playout(game, player):
    current = player

    while True:
        result = game.winner()

        if result is not None:
            return result

        move = random.choice(game.available_moves())
        game.make_move(move, current)

        current = 'O' if current == 'X' else 'X'


def monte_carlo_tree_search(game, simulations=1000):

    best_move = None
    best_score = -1

    for move in game.available_moves():

        wins = 0

        for _ in range(simulations):

            temp_game = deepcopy(game)

            temp_game.make_move(move, 'X')

            result = random_playout(temp_game, 'O')

            if result == 'X':
                wins += 1

        if wins > best_score:
            best_score = wins
            best_move = move

    return best_move


# -----------------------------
# TESTING
# -----------------------------

game = TicTacToe()

game.make_move(0, 'X')
game.make_move(4, 'O')
game.make_move(1, 'X')

game.print_board()

print("Minimax Score:",
      minimax(game, 0, True))

print("Alpha Beta Score:",
      alpha_beta(game, 0, -math.inf, math.inf, True))

print("Heuristic Alpha Beta:",
      heuristic_alpha_beta(game, 3, -math.inf, math.inf, True))

print("Best Move from MCTS:",
      monte_carlo_tree_search(game, 100))
