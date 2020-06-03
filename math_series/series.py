fib_cache = {}


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
