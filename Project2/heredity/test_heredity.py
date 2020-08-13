import pytest
from heredity import *

def test_test():
    assert 1==1

def test_heredity_returns_zero_prob():
    people = load_data("Project2//heredity//data//family0.csv")
    actual = joint_probability(people, {"Harry"}, {"James"}, {"James"})
    expected = {"Lily"}
    assert expected == actual

