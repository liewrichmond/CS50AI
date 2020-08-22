import pytest
from shopping import *


def test_test():
    assert 0 == 0


def test_load_data():
    (evidence, labels) = load_data('./Project4/shopping/shopping.csv')
    assert len(evidence) == 12330
    assert len(labels) == len(evidence)
    assert evidence[0] == [0, 0.0, 0, 0.0, 1, 0.0,
                           0.2, 0.2, 0.0, 0.0, 1, 1, 1, 1, 1, 1, 0]
    assert labels[0] == 0
    assert evidence[6] == [0, 0, 0, 0, 1, 0,
                           0.2, 0.2, 0, 0.4, 1, 2, 4, 3, 3, 1, 0]
    assert labels[6] == 0


def test_train_model():
    (evidence, labels) = load_data('./Project4/shopping/shopping.csv')
    train_model(evidence, labels)
    assert 1 == 1