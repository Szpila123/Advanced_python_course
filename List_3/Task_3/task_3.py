import itertools
import functools
import timeit
import math


def primes(n: int) -> list[int]:
    primes, nums = [], [True] * (n+1)

    for i in range(2, n+1):
        if nums[i]:
            primes.append(i)
        for j in range(i, n+1, i):
            nums[j] = False

    return primes


def rozklad_imperatywna(n: int) -> list[tuple[int, int]]:
    rozklad, num = [], 2

    while n > 1:
        count = 0
        while n % num == 0:
            count += 1
            n /= num
        if count > 0:
            rozklad.append((num, count))
        num += 1

    return rozklad


def rozklad_skladana(n: int) -> list[tuple[int, int]]:
    return [(x, max([y for y in range(1, int(math.log(n, x)) + 1) if n % (x**y) == 0])) for x in primes(n) if n % x == 0]


def rozklad_funkcyjna(n: int) -> list[int]:
    return list(filter(lambda x: x[1] > 0, map(lambda x: (x, max(itertools.takewhile(lambda p: n%(x**p) == 0, range(n)))), primes(n))))


if __name__ == '__main__':
    n = 1000
    number = 10000

    for i in range (1, 100):
        print(i, ":")
        print(rozklad_imperatywna(i))
        print(rozklad_skladana(i))
        print(rozklad_funkcyjna(i))

    def test(f_name, n, number): return print(timeit.timeit(
        f'{f_name}({n})', setup=f'from __main__ import {f_name}', number=number))

    test('rozklad_imperatywna', n, number)
    test('rozklad_skladana', n, number)
    test('rozklad_funkcyjna', n, number)
