import pytest
import os
from pagerank import *


def test_test():
    assert 1 == 1

def test_crawler():
    expected = {
        "1.html":{"2.html"},
        "2.html":{"1.html", "3.html"},
        "3.html":{"2.html", "4.html"},
        "4.html":{"2.html"}
        }
    actual  = crawl(".\\Project2\\pagerank\\corpus0\\")
    assert expected == actual
    

def test_transmission_model():
    corpus = {"1.html": {"2.html", "3.html"},
              "2.html": {"3.html"},
              "3.html": {"2.html"}}
    actual = transition_model(corpus, "1.html", DAMPING)
    expected = {"1.html": 0.05, "2.html": 0.475, "3.html": 0.475}
    assert expected == actual

