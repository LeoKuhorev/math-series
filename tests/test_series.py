from math_series import __version__
from math_series.series import fib_memo, fibonacci


class TestFibonacci:
    """Test class for fibonacci function
    """

    # Pass test
    def test_fibonacci_pass_1(self):
        actual = fibonacci(3)
        expected = 2
        assert actual == expected

    # Pass test
    def test_fibonacci_pass_2(self):
        actual = fibonacci(7)
        expected = 13
        assert actual == expected

    # Pass test
    def test_fibonacci_pass_3(self):
        actual = fibonacci(22)
        expected = 17711
        assert actual == expected

    # Edge case
    def test_fibonacci_pass_4(self):
        actual = fibonacci(0)
        expected = 0
        assert actual == expected

    # Edge case
    def test_fibonacci_pass_5(self):
        actual = fibonacci(-1)
        expected = 'Number should be positive'
        assert actual == expected

    # Fail case
    def test_fibonacci_fail_1(self):
        actual = fibonacci(3)
        expected = 3
        assert actual != expected

    # Fail case
    def test_fibonacci_fail_2(self):
        actual = fibonacci(-1)
        expected = -1
        assert actual != expected

    # Fail case
    def test_fibonacci_fail_3(self):
        actual = fibonacci(22)
        expected = 22
        assert actual != expected


class TestFibMemo:

    # Pass test
    def test_fib_memo_pass_1(self):
        actual = fib_memo(3)
        expected = 2
        assert actual == expected

    # Pass test
    def test_fib_memo_pass_2(self):
        actual = fib_memo(7)
        expected = 13
        assert actual == expected

    # Pass test
    def test_fib_memo_pass_3(self):
        actual = fib_memo(22)
        expected = 17711
        assert actual == expected

    # Edge case
    def test_fib_memo_pass_4(self):
        actual = fib_memo(0)
        expected = 0
        assert actual == expected

    # Edge case
    def test_fib_memo_pass_5(self):
        actual = fib_memo(-1)
        expected = 'Number should be positive'
        assert actual == expected

    # Fail case
    def test_fib_memo_fail_1(self):
        actual = fib_memo(3)
        expected = 3
        assert actual != expected

    # Fail case
    def test_fib_memo_fail_2(self):
        actual = fib_memo(-1)
        expected = -1
        assert actual != expected

    # Fail case
    def test_fib_memo_fail_3(self):
        actual = fib_memo(22)
        expected = 22
        assert actual != expected
