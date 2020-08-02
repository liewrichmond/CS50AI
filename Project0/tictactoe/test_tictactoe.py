import tictactoe as ttt
import pytest
import copy

EMPTY = None


def test_winner_horizontal1():
    board = [["X", "X", "X"],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    assert ttt.winner(board) == "X"
    board = [["X", "X", "O"],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    assert ttt.winner(board) == None


def test_winner_diagonal1():
    board = [["X", EMPTY, "X"],
             [EMPTY, "X", EMPTY],
             [EMPTY, EMPTY, "X"]]
    assert ttt.winner(board) == "X"


def test_empty_winner():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    assert ttt.winner(board) == None


def test_terminal_empty():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    assert ttt.terminal(board) == False


def test_hasMoves():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    assert ttt.hasMoves(board) == True


def test_player_empty_board():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    assert ttt.player(board) == "X"


def test_player_non_empty_1():
    board = [["X", EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    assert ttt.player(board) == "O"


def test_player_non_empty_2():
    board = [["X", "O", EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    assert ttt.player(board) == "X"


def test_player_non_empty_3():
    board = [["X", EMPTY, "X"],
             ["O", "X", "O"],
             ["X", "O", "X"]]
    assert ttt.player(board) == "O"


def test_actions_empty_board():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    expected = set()
    for y in range(0, 3):
        for x in range(0, 3):
            expected.add((y, x))
    assert ttt.actions(board) == expected


def test_actions_one_move_left():
    board = [["X", EMPTY, "X"],
             ["O", "X", "O"],
             ["X", "O", "X"]]
    expected = set()
    expected.add((0, 1))
    assert ttt.actions(board) == expected


def test_utiltity_X_wins():
    board = [["X", "O", EMPTY],
             ["O", "X", "O"],
             ["X", EMPTY, "X"]]
    assert ttt.utility(board) == 1


def test_utiltity_O_wins():
    board = [["X", "O", "X"],
             ["O", "O", "O"],
             ["X", EMPTY, "X"]]
    assert ttt.utility(board) == -1


def test_utiltity_nobody_wins():
    board = [["X", "O", "O"],
             ["O", "X", "X"],
             ["X", "X", "O"]]
    assert ttt.utility(board) == 0


def test_result():
    board = [["X", "O", "X"],
             ["O", "O", "X"],
             ["X", EMPTY, "O"]]
    possibleMoves = ttt.actions(board)
    expected = [["X", "O", "X"],
                ["O", "O", "X"],
                ["X", "X", "O"]]
    initBoard = copy.deepcopy(board)
    assert ttt.result(board, possibleMoves.pop()) == expected
    assert board == initBoard


def test_result_throws_error():
    board = [["X", "O", "X"],
             ["O", "O", "X"],
             ["X", EMPTY, "O"]]
    with pytest.raises(ValueError):
        ttt.result(board, (1, 1))


def test_max_value_base_case():
    board = [["X", "O", "X"],
             ["O", "O", "O"],
             ["X", EMPTY, "X"]]
    assert ttt.max_value(board) == -1


def test_max_value():
    board = [["X", EMPTY, "X"],
             ["O", "O", "X"],
             [EMPTY, "X", "O"]]
    assert ttt.max_value(board) == 1


def test_min_value():
    board = [["X", EMPTY, "X"],
             ["O", "O", "X"],
             [EMPTY, "X", "O"]]
    assert ttt.min_value(board) == 0


def test_minimax():
    board = [["X", "O", "X"],
             ["X", "O", EMPTY],
             ["O", EMPTY, "X"]]
    assert ttt.minimax(board) == (2,1)

def test_minimax_blocks_move_2():
    board = [[EMPTY, EMPTY, EMPTY],
             ["O", "X", EMPTY],
             [EMPTY, "X", EMPTY]]
    assert ttt.minimax(board) == (0, 1)
