import pytest
from nim import *

def test_test():
    assert 1 == 1

def test_ai_makes_smart_move():
    ai = train(10000)
    state = [0,1,2,0]
    action = ai.choose_action(state,False)
    assert action == (2,2)