import argparse
import sys
import itertools

MAX_CHARS = 10


def create_arguments_parser() -> argparse.ArgumentParser:
    '''Create parser for cmd line'''
    parser = argparse.ArgumentParser(description='Program for simplifing text')
    parser.add_argument('word1',
                        type=str,
                        help='First word for cryptarithm',
                        action='store')
    parser.add_argument('word2',
                        type=str,
                        help='Second word for cryptarithm',
                        action='store')
    parser.add_argument('result',
                        type=str,
                        help='Result of cryptarithm',
                        action='store')
    return parser


def check_input(word_1: str, word_2: str, result: str) -> bool:
    '''Function for checking input validity'''

    'Check if number of characters is below/equal to max'
    unique_chars = set(word_1 + word_2 + result)
    if len(unique_chars) > MAX_CHARS:
        return False

    'Only alphabetic characters'
    if not word_1.isalpha() or not word_2.isalpha or not result.isalpha():
        return False

    return True


def to_num(word: str, mapping: dict[str, int]) -> int:
    '''Change word to number accoring to mapping'''
    return int(''.join([str(mapping[x]) for x in word]))


def solve_cryptarithm(word_1: str, word_2: str, result: str) -> dict[str, int]:
    '''Funciton takes two sumed words and result of crytharithm and solves it,
        return dictionary of mappings'''

    chars = list(set(word_1 + word_2 + result))
    perms = itertools.permutations(range(MAX_CHARS), len(chars))

    for perm in perms:
        mapping = dict(zip(chars, perm))
        if to_num(word_1, mapping) + to_num(word_2, mapping) == to_num(result, mapping):
            break
    else:
        mapping = {}

    return mapping


if __name__ == '__main__':
    # Parse command arguments
    args = create_arguments_parser().parse_args(sys.argv[1:])

    words = [x.lower() for x in [args.word1, args.word2, args.result]]

    # Check input
    if not check_input(*words):
        print('Input is invalid')
        exit(1)

    # Solve
    result = solve_cryptarithm(*words)

    # Print result
    if result:

        max_len = max([len(x) for x in words])
        for word in words:
            print(f'{word:>{max_len}}  {"".join(map(lambda x: str(result[x]), word)):>{max_len}}')

        print('\nSolution:')
        for key, val in result.items():
            print(f"{key} = {val}")
    else:
        print('Solution not found')
