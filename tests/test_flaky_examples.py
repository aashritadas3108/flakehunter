import random


def test_stable_addition():
    assert 2 + 3 == 5


def test_stable_string_comparison():
    assert "flake" == "flake"


def test_intermittent_failure():
    # An intentionally unpredictable test for FlakeHunter
    assert random.random() < 0.5
