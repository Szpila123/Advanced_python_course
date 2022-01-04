"""List 2 Task 2"""


def sqrt(n: float) -> int:
    '''Count floor of the sqrt(n)'''
    if n < 0:
        raise ArithmeticError()

    if n < 1:
        return 0

    sum, i = 0, 0
    while sum < n:
        i += 1
        sum += 2 * i + 1
    return i
