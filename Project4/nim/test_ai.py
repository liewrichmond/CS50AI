import pytest
from nim import *

def test_test():
    assert 1 == 1

def test_ai_makes_smart_move():
    ai = train(100000)
    state = [0,2,1,0]
    action = ai.choose_action(state,False)
    assert action == (1,2)