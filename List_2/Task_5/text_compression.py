import itertools
def compress(text: str) -> list[tuple[int,str]]:
    '''Function used for compression, text cannot contain numbers'''
    result, idx = [], 0

    while idx < len(text):
        char = text[idx]
        char_cnt = len(list(itertools.takewhile(lambda x: x == char, text[idx:])))
        result.append((char_cnt, char))
        idx += char_cnt

    return result


def decompress(archive: list[tuple[int,str]]) -> str:
    '''Function used for decompression'''
    result = ''

    for length, char in archive:
        result += char * length

    return result

MIN_STR_LEN = 2
def save(file_name: str, archive: list[tuple[int, str]]):
    '''Function used for saving archives to files'''
    with open(file_name, 'w') as file:
        for length, char in archive:
            if length < MIN_STR_LEN: 
                length = ''
            file.write(f'{length}{char}')

def load(file_name: str) -> list[tuple[int,str]]:
    '''Function used for loading archives from files'''
    with open(file_name, 'r') as file:
        content = ' '.join(file.readlines())

    idx, result = 0, []
    while idx < len(content):
        char, number = content[idx], 1
        if char.isdigit():
            digits = ''.join(itertools.takewhile(lambda x: x.isdigit(), content[idx:]))
            idx += len(digits)
            number = int(digits)
            char = content[idx]
        result.append((number, char))
        idx += 1

    return result