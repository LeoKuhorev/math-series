import time


fib_cache = {}
lucas_cache = {}


def timing(func):
    """Decorator for counting function execution time
    Thanks to: https://stackoverflow.com/questions/5478351/python-time-measure-function
    """
    def wrap(*args):
        time1 = time.time()
        ret = func(*args)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(
            func.__name__, (time2 - time1) * 1000.0))

        return ret
    return wrap


def fibonacci(n: int) -> int:
    """Function for counting n-th number of fibonacci sequence

    Args:
        n (int): Number of fibonacci sequence

    Returns:
        int: Value for the n-th number of fibonacci sequence
    """
    if n < 0:
        return 'Number must be positive'
    elif n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fib_memo(n: int) -> int:
    """Function for counting n-th number of fibonacci sequence using memoization

    Args:
        n (int): Number of fibonacci sequence

    Returns:
        int: Value for the n-th number of fibonacci sequence
    """
    if n in fib_cache:
        val = fib_cache[n]
    elif n < 0:
        val = 'Number must be positive'
    elif n < 2:
        val = n
    else:
        val = fib_memo(n - 1) + fib_memo(n - 2)

    fib_cache[n] = val

    return val


def lucas_memo(n: int) -> int:
    """Function for counting n-th number of Lucas sequence using memoization

    Args:
        n (int): Number of Lucas sequence

    Returns:
        int: Value for the n-th number of Lucas sequence
    """
    if n in lucas_cache:
        val = lucas_cache[n]
    elif n < 1:
        val = 'Number must be greater that 0'
    elif n == 1:
        val = 2
    elif n == 2:
        val = 1
    else:
        val = lucas_memo(n - 1) + lucas_memo(n - 2)

    lucas_cache[n] = val

    return val


def sum_series(n: int, prev: int = 0, curr: int = 1) -> int:
    """Function for calculating a value for the given index of the sequence starting with arbitrary values

    Args:
        n (int): number of element
        prev (int, optional): value of the first element. Defaults to 0.
        curr (int, optional): value of the second element. Defaults to 1.

    Returns:
        int: Value of the element at given index
    """
    for i in range(n):
        prev, curr = curr, prev + curr
    return curr


# Measuring execution time for the element
n = 30


@timing
def time_fibonacci():
    print(fibonacci(n))


@timing
def time_fib_memo():
    print(fib_memo(n))


time_fibonacci()
time_fib_memo()
