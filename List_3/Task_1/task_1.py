import itertools
import functools
import timeit


def pierwsze_imperatywna(n: int) -> list[int]:
    pierwsze = []

    for i in range(2, n+1):
        for x in range(2, int(i**0.5)+1):
            if i % x == 0:
                break
        else:
            pierwsze.append(i)

    return pierwsze


def pierwsze_skladana(n: int) -> list[int]:
    temp_list = [[y for y in range(2, int(x**0.5)+1) if x % y == 0] for x in range(2, n+1)]
    return [x for x in range(2, (n+1)) if len(temp_list[x-2]) == 0]


def pierwsze_funkcyjna(n: int) -> list[int]:
    return list(filter(lambda x: all(map(lambda y: x%y != 0, range(2, int(x**0.5) + 1))), range(2, n+1)))


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
