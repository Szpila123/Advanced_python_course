def sqrt(n: float) -> int:
    '''Count floor of the sqrt(n)'''
    sum, i = 0, 0
    while sum < n:
        i += 1
        sum += 2 * i + 1
    return i
