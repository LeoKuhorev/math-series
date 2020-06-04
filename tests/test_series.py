from math_series import __version__
from math_series.series import fib_memo, fibonacci, lucas_memo, sum_series


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
        expected = 'Number must be positive'
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
    """Test class for fibonacci function with memoization
    """

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
        expected = 'Number must be positive'
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


class TestFibLucas:
    """Test class for Lucas sequence function
    """

    # Pass test
    def test_lucas_memo_pass_1(self):
        actual = lucas_memo(3)
        expected = 3
        assert actual == expected

    # Pass test
    def test_lucas_memo_pass_2(self):
        actual = lucas_memo(7)
        expected = 18
        assert actual == expected

    # Pass test
    def test_lucas_memo_pass_3(self):
        actual = lucas_memo(22)
        expected = 24476
        assert actual == expected

    # Edge case
    def test_lucas_memo_pass_4(self):
        actual = lucas_memo(1)
        expected = 2
        assert actual == expected

    # Edge case
    def test_lucas_memo_pass_5(self):
        actual = lucas_memo(-1)
        expected = 'Number must be greater that 0'
        assert actual == expected

    # Fail case
    def test_lucas_memo_fail_1(self):
        actual = lucas_memo(3)
        expected = 2
        assert actual != expected

    # Fail case
    def test_lucas_memo_fail_2(self):
        actual = lucas_memo(-1)
        expected = -1
        assert actual != expected

    # Fail case
    def test_lucas_memo_fail_3(self):
        actual = lucas_memo(22)
        expected = 22
        assert actual != expected


class TestSumSeries:
    """Test class for sum_series function
    """

    # Pass test
    def test_sum_series_pass_1(self):
        actual = sum_series(3)
        expected = 3
        assert actual == expected

    # Pass test
    def test_sum_series_pass_2(self):
        actual = sum_series(7)
        expected = 21
        assert actual == expected

    # Pass test
    def test_sum_series_pass_3(self):
        actual = sum_series(22)
        expected = 28657
        assert actual == expected

    # Edge case
    def test_sum_series_pass_4(self):
        actual = sum_series(1)
        expected = 1
        assert actual == expected

    # Fail case
    def test_sum_series_fail_1(self):
        actual = sum_series(3)
        expected = 2
        assert actual != expected

    # Fail case
    def test_sum_series_fail_2(self):
        actual = sum_series(-1)
        expected = -1
        assert actual != expected

    # Fail case
    def test_sum_series_fail_3(self):
        actual = sum_series(22)
        expected = 22
        assert actual != expected
