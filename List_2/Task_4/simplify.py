import random


def simplify(text: str, max_word_len: int, word_cnt: int) -> str:
    '''Simplify text by removing too long words and bringing down word count'''
    words = list(filter(lambda x: len(x) < max_word_len, text.split()))
    if len(words) <= word_cnt: return words
    return ' '.join(random.choices(words, k=word_cnt))
