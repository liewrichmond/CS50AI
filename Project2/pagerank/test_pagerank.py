import pytest
import os
from pagerank import *


def test_test():
    assert 1 == 1


def test_crawler():
    expected = {
        "1.html": {"2.html"},
        "2.html": {"1.html", "3.html"},
        "3.html": {"2.html", "4.html"},
        "4.html": {"2.html"}
    }
    actual = crawl(".\\Project2\\pagerank\\corpus0\\")
    assert expected == actual


def test_transmission_model():
    corpus = {"1.html": {"2.html", "3.html"},
              "2.html": {"3.html"},
              "3.html": {"2.html"}}
    actual = transition_model(corpus, "1.html", DAMPING)
    expected = {"1.html": 0.05, "2.html": 0.475, "3.html": 0.475}
    assert expected == actual


def test_transmission_model_empty_links():
    corpus = {"1.html": {},
              "2.html": {"3.html"},
              "3.html": {"2.html"}}
    actual = transition_model(corpus, "1.html", DAMPING)
    val = 1/3
    expected = {"1.html": val, "2.html": val, "3.html": val}
    assert expected == actual
    actual = transition_model(corpus, "2.html", DAMPING)
    expected = {"1.html": 0.05, "2.html": 0.05, "3.html": 0.9}
    assert expected == actual


def test_get_page():
    corpus = {"1.html": {"2.html", "3.html"},
            "2.html": {"3.html"},
            "3.html": {"2.html"}}
    prob_dist = transition_model(corpus, "1.html", DAMPING)
    page = get_page(prob_dist)

def test_sample_pagerank():
    corpus = crawl(".\\Project2\\pagerank\\corpus0\\")
    sample_pagerank(corpus, DAMPING, SAMPLES)

def test_has_converged():
    d1 = {"a":0.1, "b":0.2, "c":0.3}
    d2 = {"a":0.100001, "b":0.200001, "c":0.300001}
    d3 = {"a":0.110001, "b":0.210001, "c":0.310001}
    assert has_converged(d1,d2) == True
    assert has_converged(d1, d3) == False

def test_iterate_page_rank():
    corpus = crawl(".\\Project2\\pagerank\\corpus2\\")
    print(corpus)
    iterate_pagerank(corpus, DAMPING)
    assert 0 == 1

def test_iterate_page_rank_2():
    corpus = {"1.html": {},
        "2.html": {"3.html"},
        "3.html": {"2.html"}}
    sampled = sample_pagerank(corpus, DAMPING, SAMPLES)
    iterated = iterate_pagerank(corpus, DAMPING)
    assert sampled == iterated
