import numpy as np
import pytest
from traffic import load_data

def test_test():
    assert 1 == 1 

def test_load_data():
    images, labels = load_data('gtsrb-small')
    img_dim = (30,30,3)
    assert len(images) == len(labels)
    for img in images:
        assert img.shape == img_dim