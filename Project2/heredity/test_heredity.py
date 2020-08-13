import pytest
import math
from heredity import *

def test_test():
    assert 1==1

def test_joint_probability_family_0():
    people = load_data("Project2//heredity//data//family0.csv")
    actual = joint_probability(people, {"Harry"}, {"James"}, {"James"})
    expected = 0.0026643247488
    actual = joint_probability(people, {"Lily"}, {"James"}, {"James"})
    expected = 8.4942*10**-9
    larger = max(expected, actual)
    smaller = min(expected, actual)
    assert larger-smaller <= 0.001

def test_update():
    people = load_data("Project2//heredity//data//family0.csv")
    p = joint_probability(people, {"Harry"}, {"James"}, {"James"})
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }
    update(probabilities, {"Harry"}, {"James"}, {"James"}, p)
    assert probabilities["Harry"]["gene"][1] == p
    assert probabilities["James"]["gene"][2] == p
    assert probabilities["Lily"]["gene"][0] == p

    assert probabilities["Lily"]["trait"][False] == p
    assert probabilities["Harry"]["trait"][False] == p
    assert probabilities["James"]["trait"][True] == p

def test_update_2():
    people = load_data("Project2//heredity//data//family0.csv")
    p = joint_probability(people, {"Lily"}, {"James"}, {"James"})
    expected = 4.2471*10**-7
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }
    update(probabilities,  {"Lily"}, {"James"}, {"James"}, p)
    assert math.isclose(probabilities["Harry"]["gene"][0],expected)
    assert math.isclose(probabilities["Harry"]["gene"][1],0)
    assert math.isclose(probabilities["Harry"]["gene"][2],0)

    assert math.isclose(probabilities["James"]["gene"][0], 0)
    assert math.isclose(probabilities["James"]["gene"][1], 0)
    assert math.isclose(probabilities["James"]["gene"][2], expected)

    assert math.isclose(probabilities["Lily"]["gene"][0], 0)
    assert math.isclose(probabilities["Lily"]["gene"][1], expected)
    assert math.isclose(probabilities["Lily"]["gene"][2], 0)

    assert math.isclose(probabilities["Lily"]["trait"][True], 0)
    assert math.isclose(probabilities["Lily"]["trait"][False], expected)

    assert math.isclose(probabilities["Harry"]["trait"][True], 0)
    assert math.isclose(probabilities["Harry"]["trait"][False], expected)
    
    assert math.isclose(probabilities["James"]["trait"][True], expected)
    assert math.isclose(probabilities["James"]["trait"][False], 0)

def test_normalize():
    probabilities = {
        "Harry": {
            "gene": {
                2: 0.1,
                1: 0.2,
                0: 0.1
            },
            "trait": {
                True: 0.2,
                False: 0.6
            }
        }
    }
    normalize(probabilities)
    s_g = 0
    s_t = 0
    for gene in probabilities["Harry"]["gene"]:
        s_g += probabilities["Harry"]["gene"][gene]
    for trait in probabilities["Harry"]["trait"]:
        s_t += probabilities["Harry"]["trait"][trait]
    assert s_g == 1
    assert s_t == 1