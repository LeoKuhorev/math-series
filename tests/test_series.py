from math_series import __version__
from math_series.series import fibonacci


# Pass test
def test_fibonacci_pass_1():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


# Pass test
def test_fibonacci_pass_2():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected


# Pass test
def test_fibonacci_pass_3():
    actual = fibonacci(22)
    expected = 17711
    assert actual == expected


# Edge case
def test_fibonacci_pass_4():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


# Edge case
def test_fibonacci_pass_5():
    actual = fibonacci(-1)
    expected = 'Number should be positive'
    assert actual == expected


# Fail case
def test_fibonacci_fail_1():
    actual = fibonacci(3)
    expected = 3
    assert actual != expected


# Fail case
def test_fibonacci_fail_2():
    actual = fibonacci(-1)
    expected = -1
    assert actual != expected


# Fail case
def test_fibonacci_fail_3():
    actual = fibonacci(22)
    expected = 22
    assert actual != expected
