import pytest


def nemtel(a, b):
    devidering = a/b
    return devidering


def test_nemtel():
    assert nemtel(7, 9) == 8


def test_nemtel2():
    assert nemtel(10, 5) == 2


def test_nemtel3():
    assert nemtel(4, 8) == 0.5