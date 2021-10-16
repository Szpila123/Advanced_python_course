import random as rnd


class CoinThrow():
    """Class simulates coin throws"""
    _RND_BITS_CNT = 32

    @classmethod
    def avg_throws(cls, series_len: int = 3, tries: int = 100) -> float:
        """Return average of how many coin tosses took to get {series_len} same results 
        from {tries} samples"""
        to_rand = max(cls._RND_BITS_CNT, series_len)
        to_find = ('1' * series_len, '0' * series_len)
        sum = 0
        for _ in range(tries):
            val, position, dumped = "", 0, 0
            while not position:
                dumped += max(len(val)-series_len+1, 0)
                val = val[-series_len+1:] + \
                    format(rnd.getrandbits(to_rand), f'0{to_rand}b')

                for series in to_find:
                    idx = val.find(series)
                    if idx != -1 and (not position or position > idx + series_len):
                        position = idx + series_len

            sum += position + dumped
        return sum/tries

    @classmethod
    def avg_throws_smp(cls, series_len: int = 3, tries: int = 100) -> float:
        """Return average of how many coin tosses took to get {series_len} same results 
        from {tries} samples"""
        sum = 0
        for _ in range(tries):
            last_num, length = 0, 0
            while length < series_len:
                sum += 1
                if rnd.randrange(2) == last_num:
                    length += 1
                else:
                    last_num, length = [1, 0][last_num], 1
        return sum/tries
