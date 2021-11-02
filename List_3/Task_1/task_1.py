import itertools
import functools
import timeit


def is_prime(n: int) -> bool:
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


def pierwsze_imperatywna(n: int) -> list[int]:
    pierwsze = []

    for i in range(2, n+1):
        if is_prime(i):
            pierwsze.append(i)

    return pierwsze


def pierwsze_skladana(n: int) -> list[int]:
    return [x for x in range(2, (n+1)) if is_prime(x)]


def pierwsze_funkcyjna(n: int) -> list[int]:
    return list(filter(is_prime, range(2, n+1)))


if __name__ == '__main__':
    n = 1000
    number = 1000

    def test(f_name, n, number): return print(timeit.timeit(
        f'{f_name}({n})', setup=f'from __main__ import {f_name}', number=number))

    print(pierwsze_imperatywna(100))
    print(pierwsze_skladana(100))
    print(pierwsze_funkcyjna(100))

    test('pierwsze_imperatywna', n, number)
    test('pierwsze_skladana', n, number)
    test('pierwsze_funkcyjna', n, number)
