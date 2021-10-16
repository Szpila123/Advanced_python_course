class Prefix():

    @classmethod
    def common_prefix(cls, words: list[str], n: int = 3) -> str:
        """Returns longest prefix that appears in at least {n} words"""
        if not words or n > len(words):
            return ""

        buf = sorted(map(str.lower, words))
        best_prefix = ""

        for idx in range(n - 1, len(buf)):
            search = True
            while search:
                prefix, search = buf[idx][:len(best_prefix)+1], False
                for word in buf[idx - n + 1:idx]:
                    if not word.startswith(prefix):
                        break
                else:
                    best_prefix, search = prefix, True

        return best_prefix
