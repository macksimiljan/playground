def fib(n: int) -> int:
    if n < 1:
        raise ValueError('n has to be an integer, starting with 1!')

    if n == 1:
        return 0

    if n == 2:
        return 1

    return fib(n-1) + fib(n-2)


def fib_loop(n: int) -> int:
    if n < 1:
        raise ValueError('n has to be an integer, starting with 1!')

    numbers = [0, 1]
    while len(numbers) < n:
        next_number = numbers[-1] + numbers[-2]
        numbers.append(next_number)

    return numbers[n - 1]
