import pytest
from crossword import Crossword
from generate import CrosswordCreator

def test_test():
    assert 1 == 1 

def test_test_fail():
    assert 0 != 1

def test_enforce_node_consistency():
    crossword = Crossword("./Project3/crossword/data/structure0.txt", "./Project3/crossword/data/words0.txt")
    creator = CrosswordCreator(crossword)
    creator.enforce_node_consistency()
    for var in creator.domains:
        for word in creator.domains[var]:
            assert len(word) == var.length
