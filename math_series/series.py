import time


fib_cache = {}


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
    """Function for counting n-th number of fibonacci sequence using memoization

    Args:
        n (int): Number of fibonacci sequence

    Returns:
        int: Value for the n-th number of fibonacci sequence
    """
    if n < 0:
        return 'Number should be positive'
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
        val = 'Number should be positive'
    elif n < 2:
        val = n
    else:
        val = fib_memo(n - 1) + fib_memo(n - 2)

    fib_cache[n] = val

    return val


# Measuring execution time
n = 30


@timing
def time_fibonacci():
    print(fibonacci(n))


@timing
def time_fib_memo():
    print(fib_memo(n))


time_fibonacci()
time_fib_memo()
