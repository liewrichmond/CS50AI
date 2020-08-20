import pytest
from crossword import Crossword, Variable
from generate import CrosswordCreator


def test_test():
    assert 1 == 1


def test_test_fail():
    assert 0 != 1


def test_enforce_node_consistency():
    crossword = Crossword("./Project3/crossword/data/structure0.txt",
                          "./Project3/crossword/data/words0.txt")
    creator = CrosswordCreator(crossword)
    creator.enforce_node_consistency()
    for var in creator.domains:
        for word in creator.domains[var]:
            assert len(word) == var.length
    x = Variable(4, 1, 'across', 4)
    y = Variable(0, 1, 'down', 5)
    assert creator.domains[x] == {'FOUR', 'FIVE', 'NINE'}
    assert creator.domains[y] == {'THREE', 'SEVEN', 'EIGHT'}


def test_revise():
    crossword = Crossword("./Project3/crossword/data/structure0.txt",
                          "./Project3/crossword/data/words0.txt")
    creator = CrosswordCreator(crossword)
    creator.enforce_node_consistency()
    x = Variable(4, 1, 'across', 4)
    y = Variable(0, 1, 'down', 5)
    assert creator.revise(x, y) == True
    assert creator.domains[x] == {'NINE'}


def test_get_neighbors():
    crossword = Crossword("./Project3/crossword/data/structure0.txt",
                          "./Project3/crossword/data/words0.txt")
    creator = CrosswordCreator(crossword)
    creator.enforce_node_consistency()
    x = Variable(4, 1, 'across', 4)
    actual = (creator.crossword.neighbors(x))
    expected = {Variable(0, 1, 'down', 5), Variable(1, 4, 'down', 4)}
    assert actual == expected


def test_ac3():
    crossword = Crossword("./Project3/crossword/data/structure0.txt",
                          "./Project3/crossword/data/words0.txt")
    creator = CrosswordCreator(crossword)
    creator.enforce_node_consistency()
    actual = creator.ac3()
    expected = True
    assert expected == actual
    across_3 = Variable(0, 1, 'across', 3)
    down_5 = Variable(0, 1, 'down', 5)
    acrross_4 = Variable(4, 1, 'across', 4)
    down_4 = Variable(1, 4, 'down', 4)
    assert creator.domains[across_3] == {"SIX"}
    assert creator.domains[down_5] == {"SEVEN"}
    assert creator.domains[acrross_4] == {"NINE"}
    assert creator.domains[down_4] == {"FIVE", "NINE"}


def test_order_domain_values():
    crossword = Crossword("./Project3/crossword/data/structure0.txt",
                          "./Project3/crossword/data/words0.txt")
    creator = CrosswordCreator(crossword)
    creator.enforce_node_consistency()
    creator.ac3()
    across_3 = Variable(0, 1, 'across', 3)
    creator.order_domain_values(across_3, dict())

def test_order_domain_values_2():
    crossword = Crossword("./Project3/crossword/data/test.txt",
                          "./Project3/crossword/data/test_words.txt")
    creator = CrosswordCreator(crossword)
    creator.enforce_node_consistency()
    across_3 = Variable(0, 0, 'across', 3)
    expected = ['BAT','DAT','CAT']
    actual = creator.order_domain_values(across_3, dict())
    assert expected == actual

def test_select_unassigned_variable():
    crossword = Crossword("./Project3/crossword/data/test.txt",
                          "./Project3/crossword/data/test_words.txt")
    creator = CrosswordCreator(crossword)
    creator.enforce_node_consistency()
    actual = creator.select_unassigned_variable(dict())
    expected = Variable(0, 0, 'across', 3)
    assert expected == actual

def test_solve():
    crossword = Crossword("./Project3/crossword/data/structure0.txt",
                          "./Project3/crossword/data/words0.txt")
    creator = CrosswordCreator(crossword)
    creator.solve()