import pytest
import traffic

def test_test():
    assert 1 == 1 

def test_load_data():
    traffic.load_data('traffic-small')
    assert 1 == 1