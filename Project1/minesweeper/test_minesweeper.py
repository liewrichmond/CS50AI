import pytest
from minesweeper import *
def test_test():
        assert 1 == 1

def test_known_mines_base_case():
        s = Sentence({(1,2)}, 1)
        assert s.known_mines() == {(1,2)}

def test_known_safes_base_case():
        cells = {(1,2), (2,3), (3,4)}
        s = Sentence(cells, 0)
        assert s.known_safes()  == {(1,2), (2,3), (3,4)}

def test_mark_mine_decrements_count():
        cells = {(1,2), (1,3), (2,2)}
        s = Sentence(cells, 1)
        cell = (1,2)
        s.mark_mine(cell)
        assert s.count == 0
        assert s.cells == {(1,3),(2,2)}
        assert s.known_mines() == {(1,2)}

def testGetNeighborsTopLeftCorner():
        ai = MinesweeperAI()
        neighbors = ai.get_neighbors((0,0))
        assert neighbors == {(0,1), (1,0), (1,1)}

def testGetNeighborsTopRightCorner():
        ai = MinesweeperAI()
        neighbors = ai.get_neighbors((0,7))
        assert neighbors == {(0,6), (1,6), (1,7)}

def testGetNeighborsBottomLeftCorner():
        ai = MinesweeperAI()
        neighbors = ai.get_neighbors((7,0))
        assert neighbors == {(6,0), (6,1), (7,1)}

def testGetNeighborsBottomRighttCorner():
        ai = MinesweeperAI()
        neighbors = ai.get_neighbors((7,7))
        assert neighbors == {(6,7), (6,6), (7,6)}

def testGetNeighborsMiddle():
        ai = MinesweeperAI()
        neighbors = ai.get_neighbors((3,3))
        assert neighbors == {(2,2), (2,3), (2,4), (3,2), (3,4), (4,2), (4,3), (4,4)}


