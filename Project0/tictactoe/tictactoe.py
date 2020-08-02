"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    moves = {
        X: 0,
        O: 0
    }
    for x in range(0, 3):
        for y in range(0, 3):
            player = board[y][x]
            if player != EMPTY:
                moves[player] += 1

    if moves[X] > moves[O]:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()
    for y in range(0, 3):
        for x in range(0, 3):
            if board[y][x] == EMPTY:
                possibleActions.add((y, x))
    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Check for inavlid moves
    if board[action[0]][action[1]] != None:
        raise ValueError
    resultingBoard = copy.deepcopy(board)
    resultingBoard[action[0]][action[1]] = player(board)
    return resultingBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    row = [
        {
            X: 0,
            O: 0
        },
        {
            X: 0,
            O: 0
        },
        {
            X: 0,
            O: 0
        }
    ]
    col = [
        {
            X: 0,
            O: 0
        },
        {
            X: 0,
            O: 0
        },
        {
            X: 0,
            O: 0
        }
    ]
    diag = [
        {
            X: 0,
            O: 0
        },
        {
            X: 0,
            O: 0
        }
    ]
    neighbors = {
        0: {
            0: [row[0], col[0], diag[0]],
            1: [row[0], col[1]],
            2: [row[0], col[2], diag[1]]
        },
        1: {
            0: [row[1], col[0]],
            1: [row[1], col[1], diag[0], diag[1]],
            2: [row[1], col[2]]
        },
        2: {
            0: [row[2], col[0], diag[1]],
            1: [row[2], col[1]],
            2: [row[2], col[2], diag[0]]
        }
    }

    for x in range(0, 3):
        for y in range(0, 3):
            player = board[x][y]
            if player != EMPTY:
                counters = neighbors[x][y]
                for counter in counters:
                    counter[player] += 1
                    if counter[player] == 3:
                        return player

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or not hasMoves(board):
        return True
    else:
        return False


def hasMoves(board):
    """
    Returns True is there are any valid moves in the board, False otherwise.
    """
    for y in range(0, 3):
        for x in range(0, 3):
            if board[y][x] == EMPTY:
                return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    bestAction = ()
    alpha = -math.inf
    beta = math.inf
    if player(board) == X:
        # Max player
        for action in actions(board):
            bestResult = -math.inf
            potentialResult = min_value(result(board,action), alpha, beta) 
            bestResult = max(bestResult, potentialResult)
            alpha = max(alpha, potentialResult)
            if bestResult == potentialResult:
                bestAction = action
            if alpha >= beta:
                break
    elif player(board) == O:
        bestResult = math.inf
        # Min player
        for action in actions(board):
            potentialResult = max_value(result(board,action), alpha, beta)
            bestResult = min(bestResult, potentialResult)
            beta = min(beta, potentialResult)
            if bestResult == potentialResult:
                bestAction = action
            if beta <= alpha:
                break
    return bestAction

def max_value(board, alpha, beta):
    if terminal(board) == True:
        return utility(board)
    v = -math.inf
    for action in actions(board):
        eval = min_value(result(board, action), alpha, beta)
        v = max(v, eval)
        alpha = max(alpha, eval)
        if alpha >= beta:
            break
    return v


def min_value(board, alpha, beta):
    if terminal(board) == True:
        return utility(board)
    v = math.inf
    for action in actions(board):
        eval = max_value(result(board,action), alpha, beta)
        v = min(v, eval)
        beta = min(beta, eval)
        if beta <= alpha:
            break
    return v
