import itertools
import functools
import timeit


def doskonale_imperatywna(n: int) -> list[int]:
    doskonale = []

    for i in range(2, n+1):
        sum = 0
        for num in range(1, i//2 + 1):
            if i % num == 0:
                sum += num
        if sum == i:
            doskonale.append(i)

    return doskonale


def doskonale_skladana(n: int) -> list[int]:
    temp_list = [[y for y in range(1, x//2 + 1) if x % y == 0] for x in range(2, n+1)]
    return [x for x in range(2, (n+1)) if x == sum(temp_list[x-2])]


def doskonale_funkcyjna(n: int) -> list[int]:
    return list(filter(lambda x: sum(filter(lambda y: x % y == 0, range(1, int(x//2 + 1)))) == x, range(2, n+1)))


if __name__ == '__main__':
    n = 1000
    number = 1000

    print(doskonale_imperatywna(10000))
    print(doskonale_skladana(10000))
    print(doskonale_funkcyjna(10000))

    def test(f_name, n, number): return print(timeit.timeit(
        f'{f_name}({n})', setup=f'from __main__ import {f_name}', number=number))

    test('doskonale_imperatywna', n, number)
    test('doskonale_skladana', n, number)
    test('doskonale_funkcyjna', n, number)
