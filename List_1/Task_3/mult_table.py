class MultTable():
    _MIN_LEN = 1
    _max_num_idxs = [0, -1]

    @classmethod
    def tabliczka(cls, x1: int, x2: int, y1: int, y2: int):
        """Prints multiplication table x1 to x2 times y1 to y2 (task goal)"""
        print(cls.mult_table(list(range(x1, x2)), list(range(y1, y2))))

    @classmethod
    def mult_table(cls, x: list[int], y: list[int]) -> str:
        """Returns multiplication table of two int lists"""
        if len(x) < cls._MIN_LEN or len(y) < cls._MIN_LEN:
            return

        x.sort(), y.sort()
        width = max([len(str(x[idx_x] * y[idx_y]))
                    for idx_x in cls._max_num_idxs for idx_y in cls._max_num_idxs])

        mult_str = ' '.join([' ' * width] +
                            ['{:{width}d}'.format(num, width=width) for num in x]) + '\n'
        mult_str += '\n'.join(['{:{width}d} '.format(num, width=width) + ' '.join(['{:{width}d}'.format(x_num * num, width=width)
                                                                                  for x_num in x]) for num in y])
        return mult_str
