def fibonacci(n: int) -> int:
    """Function for counting n-th number of fibonacci sequence

    Args:
        n (INT): Number of fibonacci sequence

    Returns:
        INT: Value for the n-th number of fibonacci sequence
    """
    if n < 0:
        return 'Number should be positive'
    elif n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
